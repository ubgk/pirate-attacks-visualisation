from dash import html, dcc

from utils.data import pirate_attacks


def get_selector_div(id: str = 'selector-div', className: str = 'right cell'):
    attack_types = pirate_attacks.attack_type.unique()
    attack_types = [at for at in attack_types if type(at) is str]

    vessel_types = pirate_attacks.vessel_type.unique()
    vessel_status = pirate_attacks.vessel_status.unique()

    div = html.Div(id=id,
                   className=className,
                   children=["Attack Types",
                             dcc.Dropdown(id='attack_type_selector', options=attack_types, multi=True,
                                          style={'background-color': 'var(--primary)'})]
                   )

    return div


def get_header_div(id: str = 'header-div', className: str = 'row cell'):
    div = html.Div(id=id,
                   className=className,
                   children=[html.Header('Global Maritime Pirate Attacks'),
                             html.P(
                                 'This is an interactive visualisation of Global Maritime Pirate Attacks'
                                 ' between 1993 and 2020')]
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
