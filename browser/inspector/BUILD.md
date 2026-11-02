# Build the LUCIA history workbench

Use Rust 1.95.0 with wasm32-unknown-unknown, wasm-bindgen CLI 0.2.127,
Python 3.11+ and Node 22 / Playwright 1.61.1. From the repo root:

```powershell
python browser/inspector/build-prototype.py --bindgen C:/path/to/wasm-bindgen.exe
cd browser/inspector
npm ci
npx playwright install chromium
$env:LUCIA_SITE_DIR='../../target/history-prototype'
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

In the delivered software source outside Git, run the sixteen behavior checks
with `npm run test:pages -- --grep-invert "packaged delivery|source/legal"`.
The two delivery cases require the full packaged site. Both native crates and
root/companion locks are included, so no outer workspace or chapter directory is
needed. The helper matches 41 reports to the native CLI and writes 71 repeated
host controls. Native workspace tests and companion tests run normally.

In a clean full checkout, maintainers must run `verify-foundation.py`, then build,
`package-site.py`, `verify-site.py <site> --commit <full HEAD SHA>`, the full
eighteen browser cases with default LUCIA_SITE_DIR, and `verify-source.py --site
target/history-release/LUCIA --bindgen <absolute path>`. Source replay checks
first-party manifest paths, rebuilds outside Git in a path with spaces and
reproduces all native/WASM outcomes and sixteen behavior cases. Complete source,
scoped grants, dependency/Rust notices and public hashes are verified before
artifact upload. Rebuilt binary identity across paths/platforms is not claimed.
