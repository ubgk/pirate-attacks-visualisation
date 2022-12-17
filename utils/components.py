import collections

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
    dist = collections.Counter(pirate_attacks.attack_type)
    dist = sorted(dist.items(), key=lambda x: x[1], reverse=True)  # Sort by count
    attack_types = [x for x, y in dist if str(x) != 'nan']  # Exclude nan types

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
                                 ' between 1993 and 2020.')]
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


def get_footer_div():
    footer = html.Div(id='footer-div',
                      className='row flexible',
                      children=[
                          html.Div(id='country-div',
                                   className='footer left cell',
                                   children=[html.H5(children='Country Indicators'),
                                             html.Div(id='country-viz',
                                                      children=[
                                                          html.P(
                                                              'Click on a data point to display country information!')
                                                      ]
                                                      )

                                             ]
                                   ),

                          html.Div(id='info-div',
                                   className='footer right cell',
                                   children=[
                                       html.H5(id='about-title', children='About'),
                                       html.P(id='about-paragraph',
                                              children='This interactive dashboard visualizes global maritime pirate '
                                                       'attacks. It provides a valuable resource for individuals and '
                                                       'organizations involved in global maritime trade and policy'
                                                       ' making on international maritime security. '),

                                       html.H5(children='References'),
                                       html.P(id='about-references',
                                              children=[
                                                  html.Ol(children=[
                                                      html.Li(children=[
                                                          'Vagif (2021) Global maritime pirate attacks (1993–2020), Kaggle. Available at: ',
                                                          html.A(
                                                              href='https://www.kaggle.com/datasets/n0n5ense/global-maritime-pirate-attacks-19932020',
                                                              children='https://www.kaggle.com/datasets/n0n5ense/global-maritime-pirate-attacks-19932020'),
                                                          ' (Accessed: December 17, 2022).']),
                                                      html.Li(
                                                          'Benden, P., Feng, A., Howell, C. and Dalla Riva, G.V.,'
                                                          ' 2021. Crime at Sea: A Global Database of Maritime Pirate '
                                                          'Attacks (1993–2020). Journal of Open Humanities Data, 7, '
                                                          'p.19. DOI.')
                                                  ])
                                              ])
                                   ]
                                   )

                      ])
    return footer
