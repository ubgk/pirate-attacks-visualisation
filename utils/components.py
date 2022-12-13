import string

from dash import html, dcc

from utils.data import pirate_attacks, c_map, format_colname


def get_dropdown_div(id: str = 'dropdown-div', className: str = 'right cell'):
    # 'date', 'time', 'longitude', 'latitude', 'attack_type',
    #        'location_description', 'nearest_country', 'eez_country',
    #        'shore_distance', 'shore_longitude', 'shore_latitude',
    #        'attack_description', 'vessel_name', 'vessel_type', 'vessel_status',
    #        'data_source'

    plot_types = ['attack_type', 'nearest_country', 'eez_country',
                  'vessel_type', 'vessel_status', 'data_source']

    entries = [{"label": format_colname(pt),
                "value": pt} for pt in plot_types]

    div = html.Div(id=id,
                   className=className,
                   children=["Plot Type",
                             dcc.Dropdown(id='plot-type-dropdown', options=entries, value='attack_type',
                                          multi=False, style={'background-color': 'var(--primary)'})]
                   )

    return div


def get_selector_div(id: str = 'selector-div', className: str = 'right cell'):
    attack_types = pirate_attacks.attack_type.unique()
    attack_types = [at for at in attack_types if type(at) is str]

    # vessel_types = pirate_attacks.vessel_type.unique()
    # vessel_status = pirate_attacks.vessel_status.unique()

    entries = [{"label": html.Span(id=f'{at}_selector_span',
                                   children=at,
                                   style={'color': c_map[at]}),
                "value": at} for at in attack_types]

    div = html.Div(id=id,
                   className=className,
                   children=["Attack Types",
                             dcc.Dropdown(id='attack-type-dropdown', options=entries, value=attack_types,
                                          multi=True, style={'background-color': 'var(--primary)'})]
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
