import os

import pandas as pd
import plotly.express as px
from dash import dcc


def create_map(data: pd.DataFrame, id: str = 'pirate-map') -> dcc.Graph:
    """
    Function that creates a GeoViz given a DataFrame
    :param data: A Pandas DataFrame that represents the data to visualize!
    :param id: Optional object id for the dcc.Graph object
    :return: dcc.Graph object
    """
    fig = px.scatter_mapbox(data, lat="latitude", lon="longitude",
                            hover_name="nearest_country",
                            hover_data=["vessel_name", "attack_description"],
                            color_discrete_sequence=["yellow"],
                            zoom=2)

    fig.update_layout(mapbox_style=os.environ['MAPBOX_STYLE'],
                      mapbox_accesstoken=os.environ['MAPBOX_TOKEN'])
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return dcc.Graph(
        id=id,
        figure=fig
    )
