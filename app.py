import dash
from dash import Output, Input

import utils.data
import visualizations.geo
import visualizations.hist
import visualizations.root
from utils.data import pirate_attacks

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
]

app = dash.Dash(__name__, title='Global Maritime Attacks',
                external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True)

app.layout = visualizations.root.layout
server = app.server


@app.callback(Output(component_id='map-graph', component_property='figure'),
              Output(component_id='hist', component_property='figure'),
              Input(component_id='range-slider', component_property='value'))
def update_visualization(slider):
    data = pirate_attacks.copy()

    if slider:
        data = utils.data.filter_range(slider, data)
        visualizations.geo.update_map(visualizations.geo.map, data)
        visualizations.hist.update_hist(visualizations.hist.hist_fig, data)

    return visualizations.geo.map, visualizations.hist.hist_fig


if __name__ == '__main__':
    app.run_server(debug=True)  # This seems to run settings.py once more.
