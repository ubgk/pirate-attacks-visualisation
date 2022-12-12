import collections

import pandas as pd
import plotly.graph_objects as go

import utils.data


def create_bar(data: pd.DataFrame, col: str = 'attack_type') -> go.Figure:
    """
    Function that creates a GeoViz given a DataFrame
    :param data: A Pandas DataFrame that represents the data to visualize!
    :param id: Optional object id for the dcc.Graph object
    :return: dcc.Graph object
    """

    fig = go.Figure()

    dist = collections.Counter(data[col])
    dist = sorted(dist.items(), key=lambda x: x[1], reverse=True)
    x = [x for x, y in dist]
    y = [y for x, y in dist]
    colors = [utils.data.c_map[label] for label in x]
    hist_trace = go.Bar(x=x, y=y,  marker={'color': colors})

    fig.add_trace(hist_trace)

    fig['layout']['uirevision'] = 'userpref'
    fig.update_layout(margin={"t": 0, }, paper_bgcolor="rgba(0,0,0,0)")
    fig['layout']['uirevision'] = 'userpref'

    return fig

# def update_bar(fig: go.Figure, data: pd.DataFrame):
#     fig.data[-1].visible = False
#
#     hist_trace = go.Histogram(x=data['vessel_status'])
#
#     fig.add_trace(hist_trace)
#
#     fig['layout']['uirevision'] = 'userpref'
#
#
# bar_fig = create_bar(utils.data.pirate_attacks)
