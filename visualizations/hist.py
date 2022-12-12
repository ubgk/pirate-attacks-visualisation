import pandas as pd
import plotly.graph_objects as go
import plotly
import utils.data


def create_hist(data: pd.DataFrame, col: str = 'vessel_status') -> go.Figure:
    """
    Function that creates a GeoViz given a DataFrame
    :param data: A Pandas DataFrame that represents the data to visualize!
    :param id: Optional object id for the dcc.Graph object
    :return: dcc.Graph object
    """

    fig = go.Figure()

    hist_trace = go.Histogram(x=data[col], marker={'color': plotly.colors.qualitative.Light24})

    fig.add_trace(hist_trace)

    fig['layout']['uirevision'] = 'userpref'
    fig.update_layout(margin={"t": 0, }, paper_bgcolor="rgba(0,0,0,0)")
    fig['layout']['uirevision'] = 'userpref'

    return fig


# def update_hist(fig: go.Figure, data: pd.DataFrame):
#     fig.data[-1].visible = False
#
#     hist_trace = go.Histogram(x=data['vessel_status'])
#
#     fig.add_trace(hist_trace)
#
#     fig['layout']['uirevision'] = 'userpref'
#
#
# hist_fig = create_hist(utils.data.pirate_attacks)
