# Replication Report: Hot to Go-Go — Cooling Centers in DC

**Repo:** https://github.com/yunabaek122/final_project
**Authors:** Yuna Baek, Sumner Perera, Mithila Iyer
**QMD file:** `writeup.qmd`

## Data Availability
Data is included in the repo (`Data/` directory): cooling center shapefiles, heat sensitivity index, ward boundaries, ACS demographic shapefiles, and poverty data. Static plots are pre-rendered in `pictures/`.

## Execution Status
**Successfully replicated** after one minor YAML fix. The original YAML header used old-style `output: echo: false` syntax rather than Quarto's `execute: eval: false`. Additionally, the Python code cell used `{python eval=FALSE}` (uppercase, R-style) which Quarto 1.2.x does not recognize, causing the Shiny app code to execute and fail.

**Fix applied:** Replaced the malformed YAML block with:
```yaml
format: html
execute:
  eval: false
  echo: false
```

After this fix, `writeup.qmd` rendered to HTML successfully. The QMD is structured as a narrative writeup with embedded static images — the Shiny app code is included at the end but is not intended to execute during rendering.

## Output Match
The rendered HTML matches the structure of the committed `writeup.html` (narrative text, embedded static plots). The static images (`HEI.png`, `HSI.png`, `lowincome.png`, `poc.png`, `asthma.png`, `olderadults.png`) render correctly from the `pictures/` directory.

## Blockers
- Minor YAML syntax issue (fixed for replication).
- The full interactive Shiny app (`shiny-app/app.py`) was not tested separately; it contains hardcoded paths and requires `shiny` to be installed.
