# Replication Report: Quality of Life Index for South American Countries

**Repo:** https://github.com/francescaleon12/dap2_final_project
**Author:** Francesca Leon
**QMD file:** `final_project.qmd` (format: PDF only)

## Data Availability
Partially available. The `data/` directory includes CEPAL data files, `topic_averages.xlsx`, and a `latin_america_geom/` subdirectory. However, the `latin_america_geom/` subdirectory contains only `ne_110m_admin_0_countries.shp` — the main geometry file — without the required sidecar files (`.dbf`, `.prj`, `.cpg`). Without the `.dbf` file, the shapefile has no attribute data (no country name column, etc.), rendering the map cell unable to merge with QLI results.

## Execution Status
**Not replicated.** The QMD failed at cell 8/9 with `KeyError: 'Country'` because the Natural Earth shapefile is missing its `.dbf` attribute file. Cells 1–7 executed successfully after:
1. Fixing the hardcoded path (`base_directory = '/Users/francescaleon/...'` → actual repo path)
2. Installing missing packages: `beautifulsoup4`, `tabulate`, `wbdata`, `pandas-datareader`
3. Regenerating a missing `.shx` sidecar file from the `.shp`

## Output Match
Cells 1–7 ran (QLI computation, data processing, most visualizations). The choropleth map (cell 8) failed due to the incomplete shapefile.

## Blockers
1. **Incomplete shapefile**: Only `ne_110m_admin_0_countries.shp` was committed; the `.dbf` (attribute table), `.prj` (projection), and `.cpg` (encoding) sidecar files are missing. The shapefile reads as geometry-only with no country name columns.
2. **Hardcoded path** (fixed for replication attempt): `base_directory = '/Users/francescaleon/...'`
3. **Missing packages** (installed for replication attempt): `beautifulsoup4`, `tabulate`, `wbdata`, `pandas-datareader`
