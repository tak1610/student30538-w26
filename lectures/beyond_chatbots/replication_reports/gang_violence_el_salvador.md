# Replication Report: Gang Violence in El Salvador

**Repo:** https://github.com/willsigal/DAP2_Final
**Authors:** Andy Fan, Juan Ulloa, Will Sigal
**QMD files:** `EDA_Analysis.qmd`, `Economic_Analysis.qmd`, `final_project_data_clean.qmd`

## Data Availability
Data files are included in the repo (`Data/` directory): ACLED data, World Bank development indicators, cleaned CSVs, and El Salvador shapefiles. However, shapefiles for Nicaragua, Guatemala, Honduras, Panama, Costa Rica, and Belize referenced in `EDA_Analysis.qmd` are **not** in the repo.

## Execution Status
**Not replicated.** All three QMDs contain hardcoded absolute file paths pointing to individual team members' local machines (e.g., `'/Users/willsigal/Desktop/UChicago/Fall 2025/Python Final/...'`, `'d:\\UChicago\\...'`). `EDA_Analysis.qmd` alone has 9+ hardcoded paths. Additionally, several shapefiles loaded in `EDA_Analysis.qmd` (Nicaragua, Guatemala, Honduras, Panama, Costa Rica, Belize administrative boundaries) are not present in the repository.

## Output Match
Not attempted.

## Blockers
1. **Hardcoded absolute paths** throughout all three QMDs — paths point to team members' personal machines and would require editing every data-loading line.
2. **Missing shapefiles** for Central American countries other than El Salvador.
3. The README instructs running QMDs in a specific order (data clean → EDA → economic), but hardcoded paths prevent any QMD from running.
