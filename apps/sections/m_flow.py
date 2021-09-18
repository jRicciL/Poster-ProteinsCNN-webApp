import json
import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc
from apps.sections.m_cyto_elements import get_cyto_elements_methods
import dash_cytoscape as cyto

from app import app
from dash.dependencies import Input, Output

# Cytoscape colum
cyto_canvas = html.Div(
    style={'flex': '1',
           'position': 'relative',
           'height': '100%',
           },
    children =[
        cyto.Cytoscape(
            id ='cytoscape-methods',
            className = 'plot-margin cyto-canvas',
            responsive = True,
            maxZoom = 1.1,
            minZoom = 0.7,
            zoom = 1,
            layout = {
                'name': 'preset',
                'fit': True
                },
            style = {
                # 'position': 'absolute',
                'width': '100%',
                'minHeight': '550px',
                'maxHeight': '800px',
                # 'height': '550px',
                # 'max-height': 
                'zIndex': 10,
                # 'margin': 'auto'
                },
            elements = get_cyto_elements_methods() 
        )
    ]
)

# Restart view button
restart_view_button = dbc.Button(
    "Reset view", 
    id='reset-cytoscape',
    outline=True, 
    color="primary", 
    className="mr-1",
    style={
        # 'right': '100%',
        'marginLeft': '8px',
        'zIndex': 10,
        'bottom': '8px',
        'padding': '2px 5px',
        'position':'absolute'
    }

)

row_cyto = html.Div(
    style={
        # 'position': 'fixed',
        'display': 'flex',
        'flexDirection': 'column',
        'height': '100%',
        'width': '100%'
    },
    children = [
         cyto_canvas,
         restart_view_button
        ],
)

# Texts
row_markdown = dbc.Row(
    className='row-title-content',
    children= [
       html.H2('Methodology Workflow'),
       html.P([
                html.I(className="fas fa-hand-point-down"),
                ' Click on a ',
                html.Mark('box', 
                            className='mark-red'),
                ' below to see details about the workflow.'
                ],
            style={
                'justifyContent': 'center',
                'textAlign': 'center'
            }
            )
    ]
)



col_container = dbc.Col(
    lg = 4, md = 12, sm = 12,
    className = 'col-container-methods',
    children = [
        row_markdown,
        row_cyto,
        ],
)

# Callbacks 
@app.callback(
    [
     Output('cytoscape-methods', 'layout'),
     Output('cytoscape-methods', 'zoom'),
     Output('cytoscape-methods', 'elements'),
    ],
    [Input('reset-cytoscape', 'n_clicks')]
)
def reset_layout(n_clicks):
    layout = {'name': 'preset'}
    elements = get_cyto_elements_methods()
    return [layout, 1, elements]

# Test update columns
# @app.callback(
#     [
#      Output('methods-sec-title', 'children'),
#      Output('methods-sec-subtitle', 'children')
#     ],
#     [Input('cytoscape-methods', 'tapNodeData')]
#     # [Input('reset-cytoscape', 'n_clicks')]
# )
# def displayTapNodeData(data):
#     if data == None:
#         sec_name = 'Crystal Structures'
#     else:
#         sec_name = data['label']
#         n = 'Otra opcion'
#     children_title = [sec_name]
#     return children