# Replication Report: Transportation and Public Safety

**Repo:** https://github.com/charisml/dap-ii-final-project
**Authors:** Lizzy Diaz, Charisma Lambert
**QMD file:** `final_project.qmd`

## Data Availability
**Data not available.** The `Data/` directory contains only a `.gitkeep` placeholder. The README acknowledges the dataset was too large for GitHub and mentions a Google Drive folder for the crash map HTML files, but no download link is provided in the README or the QMD.

The QMD reads from `raw_data_path = r"C:\Users\User\OneDrive - The University of Chicago\4_DAP-2\Final Project Data"` — a hardcoded Windows path to a OneDrive folder that is not publicly accessible.

## Execution Status
**Not replicated.** Without the source data (Chicago Data Portal traffic crash datasets: `traffic_crashes_crashes.csv`, `traffic_crashes_people.csv`, `ward_boundaries.geojson`), the QMD cannot run.

## Output Match
Not attempted.

## Blockers
1. **Missing data files** — the three required CSVs/GeoJSON are not in the repo and no download link is provided.
2. **Hardcoded Windows path** (`raw_data_path`) pointing to a personal OneDrive folder.
