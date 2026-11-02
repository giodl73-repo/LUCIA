"""Replay the delivered software outside Git without chapter/manuscript files."""
import argparse,hashlib,json,os,pathlib,subprocess,tempfile,zipfile
p=argparse.ArgumentParser();p.add_argument('--site',required=True,type=pathlib.Path);p.add_argument('--bindgen',required=True,type=pathlib.Path);a=p.parse_args();B=pathlib.Path(__file__).resolve().parent;C=B/'.cache';S=a.site.resolve();native=json.loads((C/'native-cases.json').read_bytes());wasm=json.loads((C/'wasm-cases.json').read_bytes());assert len(native)==len(wasm)==71
env=os.environ.copy()
for name in ['LUCIA_BASE_URL','LUCIA_EXPECTED_COMMIT','LUCIA_SITE_DIR']:env.pop(name,None)
env['LUCIA_SITE_DIR']='../../target/history-prototype'
with(C/'source-replay.log').open('wb')as output,tempfile.TemporaryDirectory(prefix='lucia source replay ')as temp:
 T=pathlib.Path(temp).resolve()
 with zipfile.ZipFile(S/'source.zip')as archive:
  for name in archive.namelist():
   path=pathlib.PurePosixPath(name);assert path.parts[0]=='LUCIA-software-source'and '..'not in path.parts and not path.is_absolute();target=T.joinpath(*path.parts);assert target.resolve().is_relative_to(T);target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(archive.read(name))
 W=T/'LUCIA-software-source';P=W/'browser/inspector';assert ' 'in str(W)and not(W/'regions').exists()and subprocess.run(['git','rev-parse','--show-toplevel'],cwd=W,capture_output=True).returncode!=0
 def run(args,cwd=W):
  result=subprocess.run([str(x)for x in args],cwd=cwd,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT);output.write(result.stdout);output.flush();assert result.returncode==0,result.stdout.decode(errors='replace')[-3000:];return result.stdout
 for manifest in [W/'Cargo.toml',P/'Cargo.toml']:
  m=json.loads(run(['cargo','+1.95.0','metadata','--locked','--format-version','1','--manifest-path',manifest]));assert all(pathlib.Path(pkg['manifest_path']).resolve().is_relative_to(W)for pkg in m['packages']if not pkg.get('source'))
 tests=run(['cargo','+1.95.0','test','--locked','--workspace']);assert b'3 passed; 0 failed'in tests
 tests=run(['cargo','+1.95.0','test','--locked','--manifest-path',P/'Cargo.toml']);assert b'4 passed; 0 failed'in tests
 run(['python',P/'build-prototype.py','--bindgen',a.bindgen.resolve()]);assert json.loads((P/'.cache/native-cases.json').read_bytes())==native
 controls=json.loads((P/'.cache/native-controls.json').read_bytes());assert controls['exact_existing_native_cli_reports']==41
 npm='npm.cmd'if os.name=='nt'else'npm';run([npm,'ci'],cwd=P);run([npm,'run','test:pages','--','--grep-invert','packaged delivery|source/legal'],cwd=P)
 stats=json.loads((P/'.cache/browser-results.json').read_bytes())['stats'];assert stats['expected']==16 and all(stats[k]==0 for k in ['skipped','unexpected','flaky']);assert json.loads((P/'.cache/wasm-cases.json').read_bytes())==wasm
 record={'outside_git':True,'path_contains_spaces':True,'chapter_manuscript_tree_absent':True,'first_party_manifest_paths_inside_source':True,'native_tests':3,'adapter_tests':4,'existing_native_cli_reports_exact':41,'browser_checks':16,'identical_rebuilt_native_responses':71,'identical_rebuilt_wasm_responses':71,'original_wasm_sha256':hashlib.sha256((S/'pkg/lucia_history_inspector_bg.wasm').read_bytes()).hexdigest(),'rebuilt_wasm_sha256':hashlib.sha256((W/'target/history-prototype/LUCIA/pkg/lucia_history_inspector_bg.wasm').read_bytes()).hexdigest(),'binary_identity_claimed':False,'dependencies_vendored':False}
(C/'source-replay.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8');print(json.dumps(record))
