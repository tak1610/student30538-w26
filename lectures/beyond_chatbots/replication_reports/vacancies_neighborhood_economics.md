# Replication Report: Vacancies and Neighborhood Economic Conditions

**Repo:** https://github.com/montgomeryel/DAPII_final
**Authors:** Griffin Sharps, Ella Montgomery, Lauren Laine
**QMD file:** `Writeup/Writeup.qmd` (format: PDF only)

## Data Availability
Data is included in the repo. The `Writeup/` directory contains all required files: `B25075_raw.csv`, `zcta_tract_cross_walk_2010_census.csv`, `col_names.json`, `vacant.csv`, `prices_income_vacancy.csv`, and several shapefiles (`census_tract_geo_data.shp`, `vacant_gdf.shp`).

## Execution Status
**Not replicated.** The QMD ran 16/25 cells successfully, then failed at cell 17 with `KeyError: 'average_price'` because the `average_price` column was never created. The root cause is a QMD formatting bug: two consecutive code cells (the `ave_price` function definition + its application) have leading spaces before their code fence markers (`` ` ``{python}` with 1 leading space), causing Quarto to not recognize them as executable Python cells. The code is treated as markdown text rather than executed, so `average_price` is never added to the dataframe.

Cells 1–16 ran successfully after:
1. Fixing the hardcoded path (`directory = r'C:\Users\laine\...'` → actual repo path)
2. Creating a flag file `B25075_raw.csv1` to bypass the Census API download (using the cached `B25075_raw.csv`)
3. Installing missing packages: `census`, `us`, `matplotlib`, `sodapy`

During execution, the SODA API calls (Chicago vacant buildings and census tract geometries) ran successfully over the network.

## Output Match
Not fully evaluated due to failure. Cells 1–16 produced data for charts/maps, but the housing price maps (which depend on `average_price`) could not be generated.

## Blockers
1. **QMD formatting bug**: Leading spaces (1 space) before code fence markers (`` ` ``{python}` and closing `` ` ``) prevent two cells from being recognized and executed by Quarto 1.2.x. The `ave_price` function and its `apply` call are thus skipped.
2. **Hardcoded Windows path** (fixed for replication attempt): `directory = r'C:\Users\laine\...'`
3. **Live API dependency**: The code makes unguarded calls to the Chicago SODA API for vacancy data and census tract geometries on every run (no local cache check). These calls succeeded during replication.
