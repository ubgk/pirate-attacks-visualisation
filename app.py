import dash

import visualizations.root

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
]

app = dash.Dash(__name__, title='Global Maritime Attacks',
                external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True)

app.layout = visualizations.root.layout
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)  # This seems to run settings.py once more.
