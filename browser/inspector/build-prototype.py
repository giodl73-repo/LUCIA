"""Build real native/WASM controls over synthetic LUCIA records; never deploy."""
import argparse,copy,hashlib,json,os,pathlib,shutil,subprocess
from resource_controls import resource_controls
p=argparse.ArgumentParser();p.add_argument('--bindgen',required=True,type=pathlib.Path);a=p.parse_args();B=pathlib.Path(__file__).resolve().parent;R=B.parents[1];env=os.environ.copy();target=pathlib.Path(env.get('CARGO_TARGET_DIR',str(R/'target/cargo'))).resolve();env['CARGO_TARGET_DIR']=str(target);env['CARGO_TARGET_WASM32_UNKNOWN_UNKNOWN_RUSTFLAGS']='-C link-arg=--max-memory=67108864'
def run(args):subprocess.run([str(x)for x in args],cwd=R,env=env,check=True)
assert subprocess.check_output([str(a.bindgen.resolve()),'--version']).decode().strip()=='wasm-bindgen 0.2.127'
# Full-checkout CI and package-site run the Git-based foundation guard explicitly.
# The corresponding software source must also build outside Git.
for args in [[],['--target','wasm32-unknown-unknown']]:run(['cargo','+1.95.0','build','--locked','--manifest-path',B/'Cargo.toml','--release',*args])
run(['cargo','+1.95.0','build','--locked','--workspace'])
site=R/'target/history-prototype/LUCIA';assert site.resolve()==R/'target/history-prototype/LUCIA'
if site.exists():shutil.rmtree(site)
shutil.copytree(B/'web',site);run([a.bindgen.resolve(),target/'wasm32-unknown-unknown/release/lucia_history_inspector.wasm','--target','web','--out-dir',site/'pkg'])
for name in ['lucia_history_inspector.d.ts','lucia_history_inspector_bg.wasm.d.ts']:
 path=site/'pkg'/name
 if path.exists():assert path.is_file()and not path.is_symlink();path.unlink()
for name in ['BUILD.md','MODEL.md']:shutil.copyfile(B/name,site/name)
C=B/'.cache';C.mkdir(exist_ok=True);h=json.loads((B/'web/example-history.json').read_bytes());profile=json.loads((B/'web/example-profile.json').read_bytes())
def text(value):return json.dumps(value,ensure_ascii=False,separators=(',',':'))
pairs=[]
def case(history=None,p=None):pairs.append((copy.deepcopy(h if history is None else history),copy.deepcopy(profile if p is None else p)))
case();case({'people_id':'empty','title':'Empty synthetic record','worldview':'Software test'}, {'profile_id':''})
for field,value in [('worldview',''),('title',''),('people_id',''),('framing_notes',['FORBIDDEN-DEMO'])]:
 changed=copy.deepcopy(h);changed[field]=value;case(changed)
changed=copy.deepcopy(h);changed['eras'][0]['events'][0]['actors']=['unknown'];case(changed)
for collection in ['persons','events']:
 changed=copy.deepcopy(h);changed['eras'][0][collection][0]['source_story_refs']=[];case(changed)
changed=copy.deepcopy(h);changed['eras'][0]['events'][0]['era_id']='missing-era';case(changed)
changed=copy.deepcopy(h);changed['eras'][0]['events'][0]['actors']=['p1'];changed['eras'].append({'era_id':'another-era','title':'Another supplied era'});changed['eras'][0]['events'][0]['era_id']='another-era';case(changed)
changed=copy.deepcopy(h);changed['eras'][0]['persons']*=2;changed['eras'][0]['events']*=2;case(changed)
changed=copy.deepcopy(h);changed['extension']={'preserve':'original'};changed['eras'][0]['events'][0]['extension']={'nested':['retained in original']};p2=copy.deepcopy(profile);p2['extension']=True;case(changed,p2)
for key,value in [('required_event_ids',['absent','absent']),('required_person_ids',['absent']),('required_story_paths',['javascript:alert(1)']),('forbidden_external_framings',[''])]:
 p2=copy.deepcopy(profile);p2[key]=value;case(p=p2)
changed=copy.deepcopy(h);changed['title']='Own α <img src=x onerror=alert(1)>';changed['eras'][0]['events'][0]['source_story_refs']=[{'path':'javascript:alert(1)','anchor':'<script>'}];case(changed)
inputs=[]
for history,p2 in pairs:
 for operation in ['validate','compare']:inputs.append({'operation':operation,'history_json':text(history),'profile_json':text(p2)})
for raw in ['{','null','{}','\ufeff'+text(h),text(h)+' {}',text(h).replace('{','{"people_id":"duplicate",',1),text(h).replace('{','{"unknown":1e400,',1)]:
 inputs.append({'operation':'validate','history_json':raw})
for raw in ['{','null','{}',text(profile)+' {}']:
 inputs.append({'operation':'compare','history_json':text(h),'profile_json':raw})
inputs.extend([{'operation':'validate','history_json':text(h),'profile_json':'{'},{'operation':'compare','history_json':text(h)}])
for field,value in [('title','x'*4097),('eras',[{'era_id':str(i),'title':'e'}for i in range(33)])]:
 changed=copy.deepcopy(h);changed[field]=value;inputs.append({'operation':'validate','history_json':text(changed)})
inputs.extend([{'operation':'validate','history_json':' '*262145},{'operation':'compare','history_json':text(h),'profile_json':' '*131073}])
inputs.extend(['{',' '*2097153])
inputs.extend(resource_controls(h,profile))
exe=target/'release'/('lucia-history-inspector-cli.exe'if os.name=='nt'else'lucia-history-inspector-cli');native_exe=target/'debug'/('lucia-history.exe'if os.name=='nt'else'lucia-history');records=[];native_checks=0
for value in inputs:
 raw=value if isinstance(value,str)else text(value);outputs=[subprocess.check_output([str(exe)],input=raw.encode(),env=env)for _ in range(2)];assert outputs[0]==outputs[1];response=json.loads(outputs[0]);records.append({'request':raw,'response':response})
 if response['kind']=='report':
  history_path=C/'native-history.json';profile_path=C/'native-profile.json';history_path.write_bytes(value['history_json'].encode());operation=value['operation'];args=[str(native_exe),'validate'if operation=='validate'else'compare',str(history_path)]
  if operation=='compare':profile_path.write_bytes(value['profile_json'].encode());args.append(str(profile_path))
  result=subprocess.run(args,capture_output=True,env=env);expected=response['findings']if operation=='validate'else response['comparison'];assert json.loads(result.stdout)==expected
  should_fail=response['counts']['error_findings']>0 if operation=='validate'else response['comparison']['status']=='hold';assert result.returncode==int(should_fail);native_checks+=1
assert [r['response']['kind']for r in records[-16:]]==['report']+['browser_refusal']*11+['report','browser_refusal','report','browser_refusal']
assert records[-16]['response']['counts']=={'eras':32,'persons':256,'events':512,'reference_entries':2048,'error_findings':0,'warning_findings':0}
(C/'native-cases.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
(C/'native-controls.json').write_text(json.dumps({'cases':len(records),'each_repeated':2,'exact_existing_native_cli_reports':native_checks,'source':'Synthetic only; no chapter corpus/material included.'},indent=2)+'\n',encoding='utf-8')
wasm=(site/'pkg/lucia_history_inspector_bg.wasm').read_bytes();print(json.dumps({'cases':len(records),'native_cli_exact':native_checks,'wasm_bytes':len(wasm),'wasm_sha256':hashlib.sha256(wasm).hexdigest()}))
