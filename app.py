import string

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
              Output(component_id='plot-name', component_property='children'),
              Input(component_id='range-slider', component_property='value'),
              Input(component_id='attack-type-dropdown', component_property='value'),
              Input(component_id='plot-type-dropdown', component_property='value'), )
def update_visualization(slider, attack_types, plot_type):
    data = pirate_attacks.copy()

    if slider or attack_types or plot_type:
        data = utils.data.filter_data(range=slider, attack_types=attack_types, df=data)
        visualizations.geo.update_map(visualizations.geo.map, data)
        bar = visualizations.hist.create_bar(data, col=plot_type)

        plot_type = string.capwords(plot_type.replace("_", " ")).replace('Eez', 'EEZ')

    return visualizations.geo.map, bar, plot_type


if __name__ == '__main__':
    app.run_server(debug=True)  # This seems to run settings.py once more.
