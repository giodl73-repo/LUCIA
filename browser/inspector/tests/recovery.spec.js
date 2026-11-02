import {test,expect} from "@playwright/test";
import fs from "node:fs";
const history=JSON.parse(fs.readFileSync(new URL("../web/example-history.json",import.meta.url),"utf8"));
const profile=JSON.parse(fs.readFileSync(new URL("../web/example-profile.json",import.meta.url),"utf8"));
const cases=JSON.parse(fs.readFileSync(new URL("../.cache/native-cases.json",import.meta.url),"utf8"));
const fault=JSON.stringify({kind:"invalid_request",message:"Synthetic lifecycle fault, not a history result or golden control."});
async function ready(page){await page.goto("./");await expect(page.locator("#compare")).toBeEnabled();await expect(page.locator("#history")).not.toHaveValue("");await expect(page.locator("#profile")).not.toHaveValue("");}
async function intercept(page){await page.addInitScript(()=>{const Actual=window.Worker;window.__workers=[];window.__sent=[];window.__hold=false;window.Worker=class{constructor(url,opts){this.actual=new Actual(url,opts);this.actual.onmessage=e=>this.onmessage?.(e);this.actual.onerror=e=>this.onerror?.(e);window.__workers.push(this);}postMessage(data){window.__sent.push(data);if(!window.__hold)this.actual.postMessage(data);}terminate(){this.terminated=true;this.actual.terminate();}};});}
function file(name,value){return{name,mimeType:"application/json",buffer:Buffer.from(typeof value==="string"?value:JSON.stringify(value))};}

test("slot reads reject stale same-slot data while preserving independent file intent",async({page})=>{
 await page.addInitScript(()=>{const actual=File.prototype.arrayBuffer;File.prototype.arrayBuffer=function(){return this.name.startsWith("slow")?new Promise(resolve=>setTimeout(()=>actual.call(this).then(resolve),300)):actual.call(this);};});await ready(page);
 const p={...profile,profile_id:"new-profile"};await page.locator("#history-file").setInputFiles(file("slow-history.json",history));await page.locator("#profile-file").setInputFiles(file("slow-profile.json",p));await page.locator("#history").fill("{");await expect(page.locator("#profile-original")).toBeEnabled();await page.waitForTimeout(450);await expect(page.locator("#history")).toHaveValue("{");await expect(page.locator("#profile")).toHaveValue(JSON.stringify(p));
 for(const slot of ["history","profile"]){const current=slot==="history"?history:profile;await page.locator("#"+slot+"-file").setInputFiles(file("slow-old.json",current));const newer=JSON.stringify(current)+" ";await page.locator("#"+slot+"-file").setInputFiles(file("new.json",newer));await expect(page.locator("#"+slot)).toHaveValue(newer);await page.waitForTimeout(450);await expect(page.locator("#"+slot)).toHaveValue(newer);}
});

for(const slot of ["history","profile"])test(`actual ${slot} read deadline preserves both current inputs`,async({page})=>{
 await page.addInitScript(()=>{const actual=File.prototype.arrayBuffer;File.prototype.arrayBuffer=function(){return this.name==="stuck.json"?new Promise(()=>{}):actual.call(this);};});await ready(page);const h=await page.locator("#history").inputValue(),p=await page.locator("#profile").inputValue();await page.locator("#"+slot+"-file").setInputFiles(file("stuck.json","{}"));await expect(page.locator("#status")).toContainText("read exceeded 5 seconds",{timeout:6500});await expect(page.locator("#history")).toHaveValue(h);await expect(page.locator("#profile")).toHaveValue(p);
});

test("example and file selections respect newer intent in both directions",async({page})=>{
 await page.addInitScript(()=>{const actual=File.prototype.arrayBuffer;File.prototype.arrayBuffer=function(){return this.name==="slow.json"?new Promise(resolve=>setTimeout(()=>actual.call(this).then(resolve),450)):actual.call(this);};});await ready(page);
 await page.route("**/example-*.json",async route=>{await new Promise(resolve=>setTimeout(resolve,350));await route.continue();});const own=JSON.stringify({...history,title:"Own history"});await page.locator("#history").fill(own);await page.locator("#example").click();const p={...profile,profile_id:"own-file"};await page.locator("#profile-file").setInputFiles(file("new.json",p));await expect(page.locator("#profile")).toHaveValue(JSON.stringify(p));await page.waitForTimeout(500);await expect(page.locator("#history")).toHaveValue(own);await expect(page.locator("#profile")).toHaveValue(JSON.stringify(p));
 await page.unroute("**/example-*.json");await page.locator("#history-file").setInputFiles(file("slow.json",{...history,title:"Old file"}));await page.locator("#example").click();await expect(page.locator("#history")).toHaveValue(/Synthetic people-history/);await page.waitForTimeout(550);expect(JSON.parse(await page.locator("#history").inputValue()).title).toBe(history.title);
});

test("whole file, UTF-8, paste, edit and drop bounds retain usable source",async({page})=>{
 await ready(page);
 for(const [slot,limit]of [["history",262144],["profile",131072]]){
  const old=await page.locator("#"+slot).inputValue();await page.locator("#"+slot+"-file").setInputFiles({name:"large.json",mimeType:"application/json",buffer:Buffer.alloc(limit+1,32)});await expect(page.locator("#status")).toContainText("file exceeds");await expect(page.locator("#"+slot)).toHaveValue(old);
  await page.locator("#"+slot+"-file").setInputFiles({name:"bad.json",mimeType:"application/json",buffer:Buffer.from([255])});await expect(page.locator("#status")).toContainText("retained");await expect(page.locator("#"+slot)).toHaveValue(old);
  expect(await page.locator("#"+slot).evaluate((field,n)=>{field.setSelectionRange(0,0);const dt=new DataTransfer();dt.setData("text/plain"," ".repeat(n));const e=new ClipboardEvent("paste",{clipboardData:dt,bubbles:true,cancelable:true});field.dispatchEvent(e);return e.defaultPrevented;},limit)).toBe(true);await expect(page.locator("#"+slot)).toHaveValue(old);
  await page.locator("#"+slot).fill(" ".repeat(limit+1));await page.locator(slot==="history"?"#validate":"#compare").click();await expect(page.locator("#status")).toContainText(slot+" exceeds");await expect(page.locator("#report")).toBeDisabled();await page.locator("#"+slot).evaluate((field,text)=>{const dt=new DataTransfer();dt.items.add(new File([text],"dropped.json",{type:"application/json"}));field.dispatchEvent(new DragEvent("drop",{dataTransfer:dt,bubbles:true,cancelable:true}));},old);await expect(page.locator("#"+slot)).toHaveValue(old);
 }
});

test("editing either slot terminates CPU and old generations or wrong IDs cannot publish",async({page})=>{
 await intercept(page);await ready(page);
 for(const slot of ["history","profile"]){await page.evaluate(()=>{window.__hold=true;const w=window.__workers.at(-1);w.saved=w.onmessage;});await page.locator("#compare").click();const value=await page.locator("#"+slot).inputValue();await page.locator("#"+slot).fill(value+" ");expect(await page.evaluate(()=>window.__workers.at(-2).terminated)).toBe(true);await expect(page.locator("#compare")).toBeEnabled();await page.evaluate(fault=>{window.__workers.at(-2).saved({data:{type:"result",id:window.__sent.at(-1).id,report:fault}});},fault);await expect(page.locator("#report")).toBeDisabled();}
 await page.locator("#compare").click();await page.evaluate(fault=>{const r=window.__sent.at(-1);window.__workers.at(-1).onmessage({data:{type:"result",id:r.id+999,report:fault}});},fault);await expect(page.locator("#status")).toContainText("Running native");await expect(page.locator("#request")).toBeDisabled();await page.evaluate(()=>{window.__hold=false;window.__workers.at(-1).actual.postMessage(window.__sent.at(-1));});await expect(page.locator("#report")).toBeEnabled();
});

test("real compute deadline, queued ready and crash preserve inputs and clear exports",async({page})=>{
 await intercept(page);await ready(page);await page.locator("#compare").click();await expect(page.locator("#report")).toBeEnabled();const h=await page.locator("#history").inputValue(),p=await page.locator("#profile").inputValue();await page.evaluate(()=>{window.__hold=true;window.__workers[0].saved=window.__workers[0].onmessage;});await page.locator("#compare").click();await expect(page.locator("#status")).toContainText("exceeded 10 seconds",{timeout:12000});await expect(page.locator("#report")).toBeDisabled();await expect(page.locator("#request")).toBeDisabled();await page.evaluate(()=>window.__workers[0].saved({data:{type:"ready"}}));await expect(page.locator("#compare")).toBeDisabled();await page.evaluate(()=>window.__hold=false);await page.locator("#restart").click();await expect(page.locator("#compare")).toBeEnabled();await page.locator("#compare").click();await expect(page.locator("#report")).toBeEnabled();await page.evaluate(()=>window.__workers.at(-1).onerror({message:"Current crash"}));await expect(page.locator("#status")).toContainText("worker failed");await expect(page.locator("#history")).toHaveValue(h);await expect(page.locator("#profile")).toHaveValue(p);await expect(page.locator("#report")).toBeDisabled();
});

test("actual startup deadline preserves edits and restart recovers",async({page})=>{
 await page.route("**/worker.js",async route=>{await new Promise(resolve=>setTimeout(resolve,13500));try{await route.continue();}catch{}});await page.goto("./");await page.locator("#history").fill("{");await page.locator("#profile").fill("[");await expect(page.locator("#status")).toContainText("startup exceeded 12 seconds",{timeout:15000});await expect(page.locator("#history")).toHaveValue("{");await expect(page.locator("#profile")).toHaveValue("[");await page.unroute("**/worker.js");await page.locator("#restart").click();await expect(page.locator("#compare")).toBeEnabled();
});

test("malformed current reports fail safely with exports cleared",async({page})=>{
 await intercept(page);await ready(page);for(const report of ["{","null",'{"kind":"report"}']){await page.evaluate(()=>window.__hold=true);await page.locator("#compare").click();await page.evaluate(report=>window.__workers.at(-1).onmessage({data:{type:"result",id:window.__sent.at(-1).id,report,elapsedMs:1}}),report);await expect(page.locator("#status")).toContainText(/unreadable|incomplete/);await expect(page.locator("#report")).toBeDisabled();await page.evaluate(()=>window.__hold=false);await page.locator("#restart").click();await expect(page.locator("#compare")).toBeEnabled();}
});

test("unavailable worker constructor retains inputs and restart recovers",async({page})=>{
 await page.addInitScript(()=>{const Actual=window.Worker;window.__constructorFailure=true;window.Worker=class{constructor(url,options){if(window.__constructorFailure)throw new Error("Injected constructor failure");return new Actual(url,options);}};});await page.goto("./");await expect(page.locator("#status")).toContainText(/unavailable/i);await expect(page.locator("#history")).not.toHaveValue("");await expect(page.locator("#compare")).toBeDisabled();const h=JSON.stringify({...history,title:"Own retained input"});await page.locator("#history").fill(h);await page.locator("#profile").fill(JSON.stringify(profile));await page.evaluate(()=>window.__constructorFailure=false);await page.locator("#restart").click();await expect(page.locator("#compare")).toBeEnabled();await expect(page.locator("#history")).toHaveValue(h);await page.locator("#compare").click();await expect(page.locator("#report")).toBeEnabled();
});

test("combined admitted maximum stays inspectable and within the viewport",async({page})=>{
 await page.setViewportSize({width:390,height:844});await ready(page);const maximum=JSON.parse(cases.at(-16).request);await page.locator("#history").fill(maximum.history_json);await page.locator("#profile").fill(maximum.profile_json);await page.locator("#compare").click();await expect(page.locator("#report")).toBeEnabled();const r=JSON.parse(await page.locator("#raw").textContent());expect(r.counts).toEqual({eras:32,persons:256,events:512,reference_entries:2048,error_findings:0,warning_findings:0});await expect(page.locator("#era option")).toHaveCount(32);expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
});
