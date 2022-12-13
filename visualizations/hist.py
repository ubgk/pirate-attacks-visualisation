import collections

import pandas as pd
import plotly.graph_objects as go
import pycountry

import utils.data

MAX_ITEMS = 15


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
    dist = [(x, y) for x, y in dist if str(x) != 'nan']
    # dist = [(x, y) if str(x) != 'nan' else ('Unknown', y) for x, y in dist]
    labels = [str(x) for x, y in dist]
    counts = [y for x, y in dist]

    if col in ['nearest_country', 'eez_country']:
        countries = [pycountry.countries.get(alpha_3=c) for c in labels]
        hovertext = [f'{c.name}, {counts[i]}' for i, c in enumerate(countries)]
        labels = [c.flag for c in countries]

    else:
        hovertext = [f'{l}, {counts[i]}' for i, l in enumerate(labels)]

    if len(labels) > MAX_ITEMS:
        other_count = sum(counts[MAX_ITEMS:])

        labels = labels[:MAX_ITEMS] + ['OTHER']
        counts = counts[:MAX_ITEMS] + [other_count]
        hovertext = hovertext[:MAX_ITEMS] + [f'Others, {other_count}']

    if col == 'attack_type':
        colors = [utils.data.c_map[label] for label in labels]

    else:
        colors = '#007eff'

    bar_trace = go.Bar(x=labels, y=counts, hovertext=hovertext, hoverinfo='text', marker={'color': colors})

    fig.add_trace(bar_trace)

    fig['layout']['uirevision'] = 'userpref'
    fig.update_layout(margin={"t": 0, }, paper_bgcolor="rgba(0,0,0,0)")

    if col in ['nearest_country', 'eez_country']:
        fig.update_layout(
            xaxis={'tickfont': {'size': 16}}
        )

    if col == 'vessel_type':
        print("max_y:", max(counts))
    fig.update_yaxes(range=[0, max(counts)])

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
