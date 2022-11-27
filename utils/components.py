from dash import html, dcc


def get_header_div(id: str = 'header-div', className: str = 'row'):
    div = html.Div(id=id,
                   className=className,
                   children=[html.Header('Global Maritime Pirate Attacks'),
                             html.P(
                                 'This is an interactive visualisation of Global Maritime Pirate Attacks'
                                 ' between 1000 and 1500 BC.')]
                   )

    return div


def get_slider_div(id: str = 'slider-container', begin: int = 1993, end: int = 2020):
    div = html.Div(id=id,
                   children=dcc.RangeSlider(begin, end, 1,
                                            id='range-slider',
                                            marks={i: {'label': str(i)} for i in
                                                   range(begin, end + 1) if
                                                   i % 2 == 0},
                                            tooltip={"placement": "bottom",
                                                     "always_visible": True}),
                   style={'margin-top': '10px'})

    return div
