"""Only the declared synthetic prototype assets may be uploaded; never deploy."""
import json,pathlib
R=pathlib.Path(__file__).resolve().parents[2];S=R/'target/history-prototype/LUCIA'
allowed={'index.html','style.css','app.js','worker.js','example-history.json','example-profile.json','BUILD.md','MODEL.md','pkg/lucia_history_inspector.js','pkg/lucia_history_inspector_bg.wasm'}
actual=set()
for p in S.rglob('*'):
 assert not p.is_symlink(),p
 if p.is_file():actual.add(p.relative_to(S).as_posix())
assert actual==allowed,actual^allowed
assert json.loads((S/'example-history.json').read_bytes())['people_id']=='demo-people'
assert json.loads((S/'example-profile.json').read_bytes())['profile_id']=='synthetic-profile'
print(json.dumps({'prototype_files':len(actual),'examples':'synthetic','chapter_manuscript_assets_included':False,'source_package_qualified':False}))
