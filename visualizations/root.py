# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import html, dcc

from utils import components

layout = html.Div(id='layout-div',
                  children=[
                      components.get_header_div(),
                      html.Div(id='viz-div',
                               className='row flexible',
                               children=[
                                   html.Div(id='map-cell',
                                            className='left cell',
                                            children=[
                                                html.Div(id='graph-div',
                                                         children=[dcc.Graph(id='map-graph')]),
                                                components.get_slider_div()
                                            ]),

                                   html.Div(id='right-column',
                                            className='right column',
                                            children=[
                                                components.get_selector_div(),
                                                components.get_dropdown_div(),
                                                html.Div(id='plot-cell',
                                                         className='right cell',
                                                         children=[html.H5(children='Vessel Status', id='plot-name'),
                                                                   dcc.Graph(id='hist')])
                                            ]),

                               ]),

                  ]
                  )
