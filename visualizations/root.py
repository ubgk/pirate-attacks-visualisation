# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import html

import visualizations.geo as geo
from utils import data

layout = html.Div(children=[
                geo.create_map(data=data.pirate_attacks)
            ]
        )
