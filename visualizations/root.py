# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import html, dcc

import visualizations.geo as geo
from utils import data
from utils import components

layout = html.Div(id='layout-div',
                  children=[
                      components.get_header_div(),
                      html.Div(id='viz-div',
                               className='container,parent-container',
                               children=[
                                   html.Div(id='map-cell',
                                            className='fixed-cell,container',
                                            children=[
                                                html.Div(id='map-container',
                                                         children=geo.create_map(data=data.pirate_attacks)),
                                                components.get_slider_div()
                                            ]),

                                   html.Div(id='plot-cell',
                                            className='flex-cell,container',
                                            children=["PLOTS HERE!"]),

                               ]),

                  ]
                  )
