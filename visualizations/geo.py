import os

import pandas as pd
import plotly.graph_objects as go

import utils.data


def create_map(data: pd.DataFrame) -> go.Figure:
    """
    Function that creates a GeoViz given a DataFrame
    :param data: A Pandas DataFrame that represents the data to visualize!
    :param id: Optional object id for the dcc.Graph object
    :return: dcc.Graph object
    """

    fig = go.Figure()

    scatter_trace = go.Scattermapbox(lat=data["latitude"],
                                     lon=data["longitude"])

    fig.add_trace(scatter_trace)

    fig.update_layout(mapbox_style=os.environ['MAPBOX_STYLE'],
                      mapbox_accesstoken=os.environ['MAPBOX_TOKEN'])
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig['layout']['uirevision'] = 'userpref'

    return fig


def update_map(fig: go.Figure, data: pd.DataFrame):
    fig.data[-1].visible = False
    fig.update_layout(showlegend=False)
    # print(f"Number of traces: {len(fig.data)}")

    scatter_trace = go.Scattermapbox(lat=data["latitude"],
                                     lon=data["longitude"],
                                     marker={'color': data['color']})

    fig.add_trace(scatter_trace)
    fig['layout']['uirevision'] = 'userpref'

    fig.data[0].showlegend = False


map = create_map(utils.data.pirate_attacks)
