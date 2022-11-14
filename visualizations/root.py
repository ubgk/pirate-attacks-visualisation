# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import os

import pandas as pd
import plotly.express as px
from dash import html, dcc

pirate_attacks = pd.read_csv("data/pirate_attacks.csv")

fig = px.scatter_mapbox(pirate_attacks, lat="latitude", lon="longitude", hover_name="nearest_country",
                        hover_data=["vessel_name", "attack_description"],
                        color_discrete_sequence=["yellow"], zoom=2, height=920)
fig.update_layout(mapbox_style=os.environ['MAPBOX_STYLE'], mapbox_accesstoken=os.environ['MAPBOX_TOKEN'])
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

layout = html.Div(children=[
    dcc.Graph(
        id='pirate-map',
        figure=fig
    )
])
