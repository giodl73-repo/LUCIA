const $=id=>document.getElementById(id);
const limits={history:262144,profile:131072};
const originals={history:null,profile:null},reads={history:0,profile:0};
let worker,generation=0,revision=0,sequence=0,exampleToken=0,ready=false,pending=null,accepted=null,startTimer,requestTimer;
const byteLength=text=>new TextEncoder().encode(text).byteLength;
const say=text=>{$("status").textContent=text;};
function buttons(disabled){$("validate").disabled=disabled;$("compare").disabled=disabled;}
function clearResult(){
  accepted=null;$("results").hidden=true;$("empty").hidden=false;
  $("report").disabled=true;$("request").disabled=true;$("raw").textContent="";
}
function stop(){
  generation++;clearTimeout(startTimer);clearTimeout(requestTimer);
  if(worker){worker.onmessage=null;worker.onerror=null;worker.terminate();}
  worker=null;ready=false;pending=null;buttons(true);
}
function fail(message){stop();clearResult();say(message+" Inputs retained. Restart the engine to retry.");}
function start(){
  stop();clearResult();const g=++generation;
  try{worker=new Worker(new URL("worker.js",import.meta.url),{type:"module"});}
  catch{fail("Worker unavailable.");return;}
  say("Loading Rust engine…");
  startTimer=setTimeout(()=>{if(g===generation)fail("Engine startup exceeded 12 seconds.");},12000);
  worker.onerror=()=>{if(g===generation)fail("Rust worker failed.");};
  worker.onmessage=({data})=>{
    if(g!==generation)return;
    if(!data||typeof data!=="object"){fail("Unreadable worker message.");return;}
    if(data.type==="ready"){
      if(ready||pending)return;
      clearTimeout(startTimer);ready=true;buttons(false);
      say("Rust engine ready. Inspect supplied records or compare the synthetic examples.");return;
    }
    if(!pending||data.id!==pending.id||pending.revision!==revision)return;
    clearTimeout(requestTimer);const request=pending;pending=null;buttons(!ready);
    if(data.type!=="result"){fail("Inspection worker failed: "+String(data.message));return;}
    let result;try{result=JSON.parse(data.report);}catch{fail("Worker returned an unreadable report.");return;}
    if(!result||typeof result!=="object"||Array.isArray(result)||typeof result.kind!=="string"){fail("Worker returned an incomplete report.");return;}
    if(result.kind!=="report"){
      clearResult();if(typeof result.message!=="string"){fail("Worker returned an incomplete diagnostic.");return;}
      say(result.kind+": "+result.message);return;
    }
    accepted={request:request.text,report:data.report,revision,result};
    try{render(result,data.elapsedMs);}catch{fail("Worker returned an incomplete report.");}
  };
}
function changed(slot){
  revision++;exampleToken++;
  for(const name of slot?[slot]:["history","profile"])reads[name]++;
  const computing=!!pending;pending=null;clearTimeout(requestTimer);clearResult();
  if(computing)start();else say(ready?"Inputs changed. Run again to refresh the result.":worker?"Loading Rust engine; current inputs retained.":"Engine unavailable; inputs retained. Restart the engine to retry.");
}
function download(name,data){
  const url=URL.createObjectURL(new Blob([data],{type:"application/json"})),link=document.createElement("a");
  link.href=url;link.download=name;link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
}
function row(parent,values){const tr=document.createElement("tr");for(const value of values){const td=document.createElement("td");td.textContent=String(value??"");tr.append(td);}parent.append(tr);}
function refs(values){return values.map(r=>r.path+(r.anchor===null?"":" [anchor: "+r.anchor+"]")).join("\n");}
function showEra(index){
  const eras=accepted.result.interpreted_history.eras,era=eras[index];$("persons").replaceChildren();$("events").replaceChildren();
  if(!era){$("era-note").textContent="No era records were supplied.";return;}
  $("era-note").textContent="Stored era: "+era.era_id+". IDs and reference paths are supplied declarations; uniqueness, source existence and container agreement are not certified.";
  for(const p of era.persons)row($("persons"),[p.person_id+" / "+p.display_name,p.role,refs(p.source_story_refs)]);
  for(const e of era.events)row($("events"),[e.event_id+" / "+e.title,e.era_id+" / "+e.event_kind+" / "+(e.year_label??"No period label"),e.consequence,"Actors: "+e.actors.join(", ")+"; places: "+e.places.join(", "),refs(e.source_story_refs)]);
}
function render(r,ms){
  $("decision").textContent=r.profile_used?"Native profile comparison: "+r.comparison.status+" · profile "+JSON.stringify(r.comparison.profile_id):"Native history validation completed";
  const c=r.counts;$("coverage").textContent=`${c.eras} era records · ${c.persons} persons · ${c.events} events · ${c.reference_entries} reference entries. Errors: ${c.error_findings}; warnings: ${c.warning_findings}.`;
  $("findings").replaceChildren();
  for(const f of r.findings)row($("findings"),[f.severity,f.code,f.location,f.message]);
  if(!r.findings.length)row($("findings"),["—","—","—","Native returned no findings; historical/source authority is not established."]);
  $("comparison").replaceChildren();$("profile-coverage").textContent="Profile was not used for history-only validation.";
  if(r.profile_used){
    const p=r.interpreted_profile,n=p.required_event_ids.length+p.required_person_ids.length+p.required_story_paths.length;
    $("profile-coverage").textContent=`Declared requirements: ${p.required_event_ids.length} events, ${p.required_person_ids.length} persons, ${p.required_story_paths.length} paths; ${p.forbidden_external_framings.length} framing patterns. `+(n?"Presence checks do not verify source contents or historical truth.":"No required IDs or story paths are declared; a pass does not imply coverage.");
    for(const [key,label]of [["missing_event_ids","Missing event IDs"],["missing_person_ids","Missing person IDs"],["missing_story_paths","Missing story paths"],["uncited_event_ids","Uncited event IDs"],["uncited_person_ids","Uncited person IDs"],["external_framing_flags","Framing-note flags"]]){
      const title=document.createElement("h3"),pre=document.createElement("pre");title.textContent=label;pre.textContent=r.comparison[key].length?r.comparison[key].join("\n"):"None returned by native comparison.";$("comparison").append(title,pre);
    }
  }
  $("projection").textContent=r.projection_notice;
  $("projection-summary").textContent="Ignored by native decoding: "+r.ignored_history_fields.length+" history fields"+(r.profile_used?"; "+r.ignored_profile_fields.length+" profile fields.":"; profile not inspected.")+" Extensions are not checked. The known-field view may materialize defaults; original inputs remain separate.";
  $("ignored").textContent=JSON.stringify({history:r.ignored_history_fields,profile:r.ignored_profile_fields},null,2);
  $("era").replaceChildren();r.interpreted_history.eras.forEach((era,i)=>{const option=document.createElement("option");option.value=String(i);option.textContent=`Record ${i+1}: ${era.title} (${era.era_id})`;$("era").append(option);});$("era").disabled=!r.interpreted_history.eras.length;showEra(0);
  $("timing").textContent="Worker computation: "+ms.toFixed(1)+" ms including report serialization; no comparative performance claim.";
  $("raw").textContent=JSON.stringify(r,null,2);$("report").disabled=false;$("request").disabled=false;$("results").hidden=false;$("empty").hidden=true;
  say("Native checks completed. Inspect findings and coverage; chapter and source authority remain separate.");
}
function run(operation){
  if(!ready||pending)return;
  for(const slot of operation==="compare"?["history","profile"]:["history"]){if(byteLength($(slot).value)>limits[slot]){clearResult();say("Browser refusal: "+slot+" exceeds its UTF-8 byte limit.");return;}}
  const text=JSON.stringify({operation,history_json:$("history").value,profile_json:$("profile").value});
  if(byteLength(text)>2097152){clearResult();say("Browser refusal: request exceeds 2 MiB UTF-8.");return;}
  clearResult();pending={id:++sequence,revision,text};buttons(true);say("Running native Rust checks…");requestTimer=setTimeout(()=>fail("Inspection exceeded 10 seconds."),10000);worker.postMessage({id:pending.id,text});
}
async function openFile(slot,file){
  const token=++reads[slot];exampleToken++;if(!file)return;
  if(file.size>limits[slot]){say("Browser refusal: "+slot+" file exceeds its byte limit. Current inputs retained.");return;}
  let timer;
  try{
    const buffer=await Promise.race([file.arrayBuffer(),new Promise((_,reject)=>{timer=setTimeout(()=>reject(new Error("File read exceeded 5 seconds.")),5000);})]);
    if(token!==reads[slot])return;
    if(buffer.byteLength>limits[slot])throw new Error("File exceeds its byte limit.");
    const text=new TextDecoder("utf-8",{fatal:true,ignoreBOM:true}).decode(buffer);
    originals[slot]=new Uint8Array(buffer);$(slot).value=text;$(slot+"-original").disabled=false;$(slot+"-origin").textContent="Last opened original: "+file.name+". Original bytes remain separate from current text.";changed(slot);say("Opened "+slot+" input. Original bytes retained; editor line endings may normalize. Run native checks to inspect it.");
  }catch(error){if(token===reads[slot])say(String(error)+" Current inputs retained.");}
  finally{clearTimeout(timer);}
}
for(const slot of ["history","profile"]){
  $(slot).addEventListener("input",()=>changed(slot));$(slot+"-file").onchange=()=>openFile(slot,$(slot+"-file").files[0]);
  $(slot+"-original").onclick=()=>{if(originals[slot])download("lucia-opened-"+slot+"-original.json",originals[slot]);};
  $(slot+"-current").onclick=()=>download("lucia-current-"+slot+".json",$(slot).value);
  $(slot+"-lf").onclick=()=>{$(slot).value=$(slot).value.replace(/^\uFEFF/,"").replace(/\r\n?/g,"\n");changed(slot);say("Current "+slot+" changed to an LF copy with leading BOM removed. Opened originals retained separately.");};
  $(slot).ondragover=e=>e.preventDefault();$(slot).ondrop=e=>{e.preventDefault();openFile(slot,e.dataTransfer.files[0]);};
  $(slot).addEventListener("paste",e=>{const field=$(slot),pasted=e.clipboardData?.getData("text/plain")||"",next=field.value.slice(0,field.selectionStart)+pasted+field.value.slice(field.selectionEnd);if(byteLength(next)>limits[slot]){e.preventDefault();say("Browser refusal: "+slot+" paste would exceed its byte limit. Current inputs retained.");}});
}
async function examples(){
  const token=++exampleToken,rev=revision;reads.history++;reads.profile++;
  try{const responses=await Promise.all([fetch("example-history.json"),fetch("example-profile.json")]);if(responses.some(r=>!r.ok))throw new Error("Synthetic example unavailable.");const[h,p]=await Promise.all(responses.map(r=>r.text()));if(token!==exampleToken||rev!==revision)return;$("history").value=h;$("profile").value=p;changed();if(ready)say("Synthetic inputs loaded. Inspect or compare them.");}
  catch(error){if(token===exampleToken)say(String(error)+" Current inputs retained.");}
}
$("restart").onclick=start;$("example").onclick=examples;$("validate").onclick=()=>run("validate");$("compare").onclick=()=>run("compare");$("era").onchange=()=>{if(accepted)showEra(Number($("era").value));};
$("request").onclick=()=>{if(accepted&&accepted.revision===revision)download("lucia-exact-request.json",accepted.request);};$("report").onclick=()=>{if(accepted&&accepted.revision===revision)download("lucia-exact-report.json",accepted.report);};
start();examples();
