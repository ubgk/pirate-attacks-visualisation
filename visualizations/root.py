# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import html, dcc

import visualizations.geo as geo
import visualizations.hist
from utils import components
from utils import data

layout = html.Div(id='layout-div',
                  children=[
                      components.get_header_div(),
                      html.Div(id='viz-div',
                               className='row',
                               children=[
                                   html.Div(id='map-cell',
                                            className='left-column',
                                            children=[
                                                html.Div(id='graph-div',
                                                         children=[dcc.Graph(id='map-graph')]),
                                                components.get_slider_div()
                                            ]),

                                   html.Div(id='right-column',
                                            className='columns',
                                            children=[html.Div(id='plot-div',
                                                               children=[dcc.Graph(id='hist')])
                                                      ]),

                               ]),

                  ]
                  )
