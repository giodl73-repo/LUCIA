import init,{inspect_request} from "./pkg/lucia_history_inspector.js";
await init();
postMessage({type:"ready"});
self.onmessage=({data})=>{
  const started=performance.now();
  try{postMessage({type:"result",id:data.id,report:inspect_request(data.text),elapsedMs:performance.now()-started});}
  catch(error){postMessage({type:"error",id:data.id,message:String(error)});}
};
