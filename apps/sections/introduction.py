import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import dash_defer_js_import as dji

from app import app

# Layout
layout = dbc.Row(
    className='section-container',
    # fluid=True,
    children = [ 
        dbc.Col(
            lg = 6,
            children=[
                # dji.Import(src="https://unpkg.com/ngl@0.10.4/dist/ngl.js"),
                html.H2('Test'),
                dcc.Input(id="in-component1", 
                          type="text", placeholder="", 
                          value = 'dfs'),
                html.Div(id='viewport'),
                html.Div(id='output-test')
            ]
        ),
        dbc.Col(
            lg = 6,
            children= [
                html.H2('Test 2'),
                dcc.Graph(
                        figure={
                            'data': [
                                {'x': [1, 2, 3], 'y': [4, 1, 2],
                                    'type': 'bar', 'name': 'SF'},
                                {'x': [1, 2, 3], 'y': [2, 4, 5],
                                'type': 'bar', 'name': u'Montréal'},
                            ]
                        }
                    ),
            ]
        )
    ]
)

app.clientside_callback(
    '''
    function (value) {
        var stage = new NGL.Stage("viewport");
        // load a PDB structure and consume the returned `Promise`
        stage.loadFile("https://raw.githubusercontent.com/jRicciL/MD_namd_python/master/dm_sources_1L2Y/1-topologia/tc5b.pdb").then(function (component) {
        // add a "cartoon" representation to the structure component
        component.addRepresentation("cartoon");
        // provide a "good" view of the structure
        component.autoView();
        });
        return value
    }
    ''',
    Output('output-test', 'children'),
    Input('in-component1',  'value'),
    # prevent_initial_call = True
)