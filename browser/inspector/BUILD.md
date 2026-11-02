# Build the LUCIA history workbench prototype

Use Rust 1.95.0 with wasm32-unknown-unknown, wasm-bindgen CLI 0.2.127,
Python 3.11+ and Node 22 / Playwright 1.61.1. From the repo root:

```powershell
python browser/inspector/build-prototype.py --bindgen C:/path/to/wasm-bindgen.exe
cd browser/inspector
npm ci
npx playwright install chromium
npm run test:pages
```

`CARGO_TARGET_DIR` can select an absolute external shared build cache. The helper
freshly builds the native control adapter and WASM, then stages only synthetic
examples, static UI, generated module and these software docs under
`target/history-prototype/LUCIA`. Private synthetic controls/captures stay in
`.cache`, not public assets. WASM linear memory is limited to 64 MiB.

Native serde 1.0.228 and serde_json 1.0.149 are retained in the independent
companion workspace, with an initial lock seeded from the native lock. Original
core, native workspace/CLI/lock, chapter content and original policy remain
unchanged. No TRACKER-relative build dependency or runtime server is required.

Complete corresponding-software packaging, notices, source replay, expanded
recovery, hosted/default/live qualification are release gates still pending.
