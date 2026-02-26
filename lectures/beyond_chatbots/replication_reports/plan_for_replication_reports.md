There are six student final projects posted here -- https://docs.google.com/document/d/19iwM159IFWMPAK9FEFMksvuieJ0bxYvWvVaZ9OLWAp0/edit?tab=t.0#heading=h.wt1ll3nqzj8l

Are they reproducible? A user such as a TA or an AI agent should be able to knit the `.qmd` file and re-generate one version of the writeup (HTML or PDF). Prefer HTML; only attempt PDF if the QMD specifies `format: pdf` and HTML is not available.

## Steps for each project

1. Check for a `README.md`. If the underlying dataset is large or not included in the repo, look for a download link in the README. Download the data and save it to the path specified in the README. The user should not need to rename any files to get the code to run.

2. Install any required packages. If a `renv.lock` is present, use `renv::restore()`. If a `requirements.txt` is present, use `pip install -r requirements.txt`. Otherwise, install packages as needed to get the code to run.

3. Knit the `.qmd` file. If it fails, attempt to debug and fix minor issues (e.g., missing package, wrong working directory). Do not spend more than ~15 minutes debugging a single project before declaring it non-replicable.

4. Write a replication report and save it to `replication_reports/<project_name>.md`. The report can be as short as one sentence if everything works or if source data are clearly unavailable. Otherwise include:
   - **Data availability**: Was the data included or downloadable?
   - **Execution status**: Did the QMD knit successfully?
   - **Output match**: Did the outputs (figures, tables, results) match the submitted writeup?
   - **Blockers**: Any errors, missing files, or environment issues encountered.

## What counts as successful replication

Replication is successful if the QMD knits without errors and produces outputs that are substantively consistent with the submitted writeup. Exact numerical matches are not required if differences are plausibly due to random seeds or minor data versioning. Note any discrepancies even when marking a project as replicated.
