import collections

import pandas as pd
import plotly.graph_objects as go

import utils.data


def create_bar(data: pd.DataFrame, col: str = 'attack_type') -> go.Figure:
    """
    Function that creates a GeoViz given a DataFrame
    :param data: A Pandas DataFrame that represents the data to visualize!
    :param col: The column to visualize!
    :return: dcc.Graph object
    """

    fig = go.Figure()

    dist = collections.Counter(data[col])
    dist = sorted(dist.items(), key=lambda x: x[1], reverse=True)
    x = [x for x, y in dist]
    y = [y for x, y in dist]

    if len(x) > 20:
        other_y = sum(y[20:])

        x = x[:20] + ['OTHER']
        y = y[:20] + [other_y]

    if col == 'attack_type':
        colors = [utils.data.c_map[label] for label in x]

    else:
        colors = '#007eff'

    bar_trace = go.Bar(x=x, y=y, marker={'color': colors})

    fig.add_trace(bar_trace)

    fig['layout']['uirevision'] = 'userpref'
    fig.update_layout(margin={"t": 0, }, paper_bgcolor="rgba(0,0,0,0)")
    fig['layout']['uirevision'] = 'userpref'

    fig.update_yaxes(range=[0, max(y)])

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
