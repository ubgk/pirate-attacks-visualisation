import functools

import pycountry
import requests
from dash import html

from utils.data import country_indicators


def fint(val):
    try:
        return f"{int(val):,}"
    except:
        return "N/A"


def fflt(val):
    if not val != val: # This is False for nan values
        return f'{val:,.1f}'
    else:
        return 'N/A'


def get_html_rows(data):
    # {'country': 'OMN', 'year': 2011.0, 'corruption_index': 4.8, 'homicide_rate': 1.0457992398, 'GDP': 20921.1459820841, 'total_fisheries_per_ton': 158723.0, 'total_military': 47000.0, 'population': 3251108.0, 'unemployment_rate': 4.62400007247925, 'totalgr': 0.479336978549306, 'industryofgdp': 0.71565548226747, 'country_name': 'Oman'}

    if data['GDP'] and data['population']:
        gdp_per_capita = (data['GDP'] * 1_000_000) / data['population']
        gdp_per_capita = fint(gdp_per_capita)
    else:
        gdp_per_capita = "N/A"

    if not data["industryofgdp"] != data["industryofgdp"]:
        industryofgdp = f'{(data["industryofgdp"] * 100):.2f}%'
    else:
        industryofgdp = 'N/A'

    data = [
        # ('Country', data['country_name']),
        ('ISO', data['country']),
        # ('Year', int(data['year'])),
        ('Population', fint(data['population'])),
        ('GDP ($M)', fint(data['GDP'])),
        # ('GDP per Capita ($)', gdp_per_capita),
        ('Unemployment Rate', fflt(data["unemployment_rate"])),
        ('Corruption Index', fflt(data["corruption_index"])),
        ('Homicide Rate', fflt(data["homicide_rate"])),
        ('Fishery Production (Tons)', fint(data['total_fisheries_per_ton'])),
        ('Total Military', fint(data['total_military'])),
        ('Industry / GDP', industryofgdp)
    ]

    data = [html.Tr([html.Td(html.B(key)), html.Td(value)]) for key, value in data]

    return data


def get_table(country_code: str, year: int):
    data = country_indicators.query('year == @year and country == @country_code').iloc[0]
    data['country_name'] = pycountry.countries.get(alpha_3=country_code).name

    table = html.Table(id='country_table',
                       children=get_html_rows(data))

    table = html.Div(id='table-container',
                     children=table)
    return table


def get_viz(country_code: str, year: int):
    flag = get_flag(country_code, year)
    table = get_table(country_code, year)

    return flag, table


@functools.lru_cache
def get_flag(country_code, year):
    url = f"https://restcountries.com/v2/alpha/{country_code}"
    response = requests.get(url)

    if response.status_code != 200:
        return "FLAG"

    response = response.json()
    svg_url = response["flags"]["svg"]

    country = pycountry.countries.get(alpha_3=country_code)
    elem = html.Div(id='flag-container',
                    children=[html.Img(id='country_flag', src=svg_url),
                              html.H6(id='flag-legend', children=f'{country.name}, {year}')])
    return elem
    # return response
