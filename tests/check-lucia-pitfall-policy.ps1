Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$root = Resolve-Path (Join-Path $PSScriptRoot "..")

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

# Checks LUCIA-PF-01: manuscript proposal must not become publication readiness.
Assert-Text "proposal, not a decision|not yet a manuscript|Six gaps remain" @(
  "docs/MANUSCRIPT-ARCHITECTURE.md",
  "README.md"
) "Expected manuscript-readiness limitation language was not found."

# Checks LUCIA-PF-02: structured history must compare against chapter authority.
Assert-Text "established story|compare against established|chapters remain the established story|product-local" @(
  "docs/people-history-engine.md",
  "README.md",
  "crates/lucia-history-core/src/lib.rs"
) "Expected established-story comparison boundary was not found."

# Checks LUCIA-PF-03: rubric learning must stay forward-only.
Assert-Text "forward only|append-only|never retroactively|retroactive rescoring is never allowed" @(
  "README.md",
  "scoring/RUBRIC.md",
  "scoring/INNOVATIONS.md",
  "skills/chronicle-innovation/SKILL.md"
) "Expected forward-only rubric language was not found."

# Checks LUCIA-PF-04: the board catalog must require selected specialists.
Assert-Text "specialist catalog, not an instruction to activate|select two or three|Record the selected role files|different angle" @(
  ".roles/ROLE.md",
  ".roles/board/ROLE.md",
  "skills/chronicle-board/SKILL.md"
) "Expected selected-board-role boundary was not found."
