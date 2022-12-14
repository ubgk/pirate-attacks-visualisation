import time

import dash
from dash import Output, Input

import utils.data
import visualizations.geo
import visualizations.hist
import visualizations.root
from utils.data import pirate_attacks, format_colname

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
]

app = dash.Dash(__name__, title='Global Maritime Attacks',
                external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True)

app.layout = visualizations.root.layout
server = app.server


@app.callback(Output(component_id='map-graph', component_property='figure'),
              Input(component_id='range-slider', component_property='value'),
              Input(component_id='attack-type-dropdown', component_property='value'),
              Input(component_id='map-graph', component_property='selectedData'))
def update_map(slider, attack_types, selected_data):
    data = pirate_attacks.copy()

    if selected_data:
        # start_time = time.time()
        ref_idx = [p['customdata'][-1] for p in selected_data['points']]
        data['gray_mask'] = data.reference_id.apply(lambda ref_id: ref_id not in ref_idx)
        data.loc[data['gray_mask'], 'shaded_color'] = 'gray'
        # print(f"Color updated in {time.time() - start_time}!")

    data = utils.data.filter_data(df=data, range=slider, attack_types=attack_types)
    visualizations.geo.update_map(visualizations.geo.map, data)

    return visualizations.geo.map


@app.callback(Output(component_id='hist', component_property='figure'),
              Output(component_id='plot-name', component_property='children'),
              Input(component_id='range-slider', component_property='value'),
              Input(component_id='attack-type-dropdown', component_property='value'),
              Input(component_id='plot-type-dropdown', component_property='value'),
              Input(component_id='map-graph', component_property='selectedData'))
def update_plot(slider, attack_types, plot_type, selected_data):
    data = pirate_attacks.copy()

    data = utils.data.filter_data(df=data, range=slider, attack_types=attack_types, selected_data=selected_data)
    bar = visualizations.hist.create_bar(data, col=plot_type)

    return bar, format_colname(plot_type)


if __name__ == '__main__':
    app.run_server(debug=True)
