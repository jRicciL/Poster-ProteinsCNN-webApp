import json
import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc
from apps.sections.m_cyto_elements import get_cyto_elements 
import dash_cytoscape as cyto

from app import app
from dash.dependencies import Input, Output

stylesheet_cyto = [
    {
            'selector': '.box',
            'style': {
                'background-color': 'red',
                'line-color': 'red'
            }
        }
]


# Restart view button
restart_view_button = dbc.Button(
    "Reset view", 
    id='reset-cytoscape',
    outline=True, 
    color="info", 
    className="mr-1",
    style={
        # 'right': '100%',
        'marginLeft': '6px',
        'zIndex': 20,
        'bottom': '36px',
        # 'marginTop': '-18px',
        'padding': '2px 5px',
        'position':'relative'
    }
)

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
                'minHeight': '560px',
                # 'maxHeight': '850px',
                # 'height': '550px',
                # 'max-height': 
                'zIndex': 10,
                # 'margin': 'auto'
                },
            elements = get_cyto_elements() ,
            # stylesheet=stylesheet_cyto
        ),
        restart_view_button
    ]
)



row_cyto = html.Div(
    style={
        'display': 'flex',
        'flexDirection': 'column',
        # 'height': '50%',
        'width': '100%'
    },
    children = [
         cyto_canvas
        #  restart_view_button
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


# col_container = dbc.Col(
#     lg = 4, md = 12, sm = 12,
#     className = 'col-container-methods',
#     children = [
#         row_markdown,
#         row_cyto,
#         ],
# )

col_contents = [
        row_markdown,
        row_cyto,
        ]

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
    elements = get_cyto_elements()
    return [layout, 1, elements]
