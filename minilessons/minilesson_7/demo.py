import pydeck as pdk
import geopandas as gpd
import streamlit as st
from os.path import join

# 1. load GeoJSON, add color/width columns
cta_file = join("minilessons/minilesson_7", "cta_rail_lines.geojson")
routes = gpd.read_file(cta_file)
routes["color"] = routes["type"].apply(
    lambda x: [255, 0, 0, 180] if x == "Subway" else [100, 100, 100, 140])
routes["width"] = routes["shape_len"].astype(float) / 5000

# 2. create layer
layer = pdk.Layer("GeoJsonLayer", data=routes,
    get_line_color="color", get_line_width="width",
    line_width_min_pixels=1, pickable=True)

# 3. create deck with view + tooltip
deck = pdk.Deck(layers=[layer],
    initial_view_state=pdk.ViewState(
        latitude=41.88, longitude=-87.63, zoom=10),
    tooltip={"html": "<b>{lines}</b><br/>Type: {type}"})

# 4. display
st.pydeck_chart(deck)
