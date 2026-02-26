# Replication Report: Carjacking Analysis in Chicago

**Repo:** https://github.com/suryahardiansyah/ppha30538-final-project
**Authors:** Astari Raihanah, Surya Hardiansyah
**QMD file:** `group_28_writeup_html.qmd`

## Data Availability
Data is included in the repo (`data/` directory): `chicago_carjackings.csv`, `chicago_neighborhoods.geojson`, `processed_carjackings.csv`.

## Execution Status
**Successfully replicated.** `group_28_writeup_html.qmd` rendered to HTML without errors. The QMD uses `execute: eval: false` (correct Quarto syntax), so code cells are displayed but not executed — matching the intent of the submitted writeup, which contains narrative text, code displays, and embedded static images from the `pictures/` directory.

Note: There is also `group_28_writeup.qmd` (PDF format), which was not attempted since an HTML version successfully rendered.

## Output Match
The rendered HTML matches the structure of the committed `group_28_writeup_html.html` (narrative, embedded figures, code shown without outputs). Substantive content appears consistent. Note: the date field renders as the literal string `` `r Sys.Date()` `` since this is a Python QMD that uses an R-style date expression.

## Blockers
None for the HTML writeup. The PDF version (`group_28_writeup.qmd`) was not tested.
