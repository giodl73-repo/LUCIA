Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$root = Resolve-Path (Join-Path $PSScriptRoot "..")
$boundaryPath = Join-Path $root "docs/history-boundaries.v1.json"

function Assert-Text {
  param(
    [string]$Pattern,
    [string[]]$Paths,
    [string]$Message
  )

  $resolved = $Paths | ForEach-Object { Join-Path $root $_ }
  $matches = Select-String -Path $resolved -Pattern $Pattern -ErrorAction Stop
  if (-not $matches) {
    throw $Message
  }
}

function Assert-Boundary {
  param(
    [object]$Manifest,
    [string]$Pitfall,
    [string]$RequiredOwner,
    [string[]]$BlockedClaims
  )

  $boundary = $Manifest.pitfall_boundaries | Where-Object { $_.pitfall -eq $Pitfall }
  if (-not $boundary) {
    throw "Missing history boundary for $Pitfall"
  }

  if ($boundary.required_owner -ne $RequiredOwner) {
    throw "Unexpected required owner for $Pitfall`: $($boundary.required_owner)"
  }

  foreach ($claim in $BlockedClaims) {
    if ($boundary.blocked_claims -notcontains $claim) {
      throw "Missing blocked claim for $Pitfall`: $claim"
    }
  }
}

if (-not (Test-Path -LiteralPath $boundaryPath)) {
  throw "Missing history boundary manifest: $boundaryPath"
}

$boundaryManifest = Get-Content -LiteralPath $boundaryPath -Raw | ConvertFrom-Json
if ($boundaryManifest.'$schema' -ne "lucia.history-boundaries.v1") {
  throw "Unexpected history boundary schema: $($boundaryManifest.'$schema')"
}

if ($boundaryManifest.authority.established_story -ne "LUCIA locked chapters and chapter-adjacent established-story profiles") {
  throw "Established-story authority must stay with locked chapters and established-story profiles."
}

if ($boundaryManifest.authority.downstream_consumer_contracts -ne "named downstream repositories") {
  throw "Downstream consumer contracts must stay with named downstream repositories."
}

# Checks LUCIA-PF-01: manuscript proposal must not become publication readiness.
Assert-Text "proposal, not a decision|not yet a manuscript|Six gaps remain" @(
  "docs/MANUSCRIPT-ARCHITECTURE.md",
  "README.md"
) "Expected manuscript-readiness limitation language was not found."
Assert-Text "production archive, not manuscript publication readiness|not yet a manuscript a reader can pick up" @(
  "README.md"
) "Expected README-local manuscript-readiness boundary was not found."

# Checks LUCIA-PF-02: structured history must compare against chapter authority.
Assert-Boundary $boundaryManifest "LUCIA-PF-02" "LUCIA locked chapters and established-story profiles" @(
  "valid people-history JSON is the established historical account",
  "compare output replaces source-cited chapter prose",
  "BANISH gamepack scores make a generic history primitive",
  "product-local Rust crates are shared portfolio contracts"
)
Assert-Text "established story|compare against established|chapters remain the established story|product-local" @(
  "docs/people-history-engine.md",
  "README.md",
  "crates/lucia-history-core/src/lib.rs"
) "Expected established-story comparison boundary was not found."

# Checks LUCIA-PF-03: rubric learning must stay forward-only.
Assert-Boundary $boundaryManifest "LUCIA-PF-03" "LUCIA rubric version custody" @(
  "new rubric version silently rescores locked chapters",
  "typology cluster rewrites historical score meaning",
  "innovation adoption changes past chapter status",
  "research summary may compare old chapters as if scored under the latest rubric"
)
Assert-Text "forward only|append-only|never retroactively|retroactive rescoring is never allowed" @(
  "README.md",
  "scoring/RUBRIC.md",
  "scoring/INNOVATIONS.md",
  "skills/chronicle-innovation/SKILL.md"
) "Expected forward-only rubric language was not found."

# Checks LUCIA-PF-04: the board catalog must require selected specialists.
Assert-Boundary $boundaryManifest "LUCIA-PF-04" "chapter review artifacts" @(
  "all board roles are active for every chapter",
  "catalog size is review coverage",
  "stale or duplicate roles remain authoritative without selection",
  "board review can omit selected role files and rationale"
)
Assert-Text "specialist catalog, not an instruction to activate|select two or three|Record the selected role files|different angle" @(
  ".roles/ROLE.md",
  ".roles/board/ROLE.md",
  "skills/chronicle-board/SKILL.md"
) "Expected selected-board-role boundary was not found."
