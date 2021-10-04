import dash.html as html
import dash.dcc as dcc
from dash.html.Mark import Mark
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, ClientsideFunction
from app import app

# Titles
row_titles = dbc.Row(
    className='row-title-content',
    children= [
        # Title
       html.H2([
           "Methods: Key takeaways",
           ]
           ),
        # html.Hr(),
       # Subtitle
    #    html.H3([
    #        'Summary of the methodology'
    #        ]
    #    )
    ]
)

summary_col = dbc.Col(
    className='row-text-content',
    sm=12, lg=6,
    children=[
        html.H3(
            [
                'Summary of the methodology'
            ],
            className='h5-header'
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H6(
                        [
                        html.Mark("1)"),
                        ' Building the conformational ensemble'
                        ], 
                            className="card-title"),
                    html.Hr(style={'margin': '0'}),
                    html.P(
                        [
                            html.Code("Crystallographic"),
                            ' and ',
                            html.Code("MD-derived"),
                            " protein conformations ",
                            html.I(className='fas fa-long-arrow-alt-right'),
                           ' ',
                            html.Code("1,524"),
                            ' structures.'
                        ],
                        className="card-text",
                    ),
                ]
            ),
            outline=True,
            className="w-80",
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H6(
                        [
                        html.Mark("2)"),
                        ' Ensemble Docking'
                        ], 
                            className="card-title"),
                    html.Hr(style={'margin': '0'}),
                    html.P(
                        [
                            html.Code("DEKOIS"),
                            ' library ',
                            html.I(className='fas fa-long-arrow-alt-right'),
                            ' ',
                            html.Code("1,200 molecules"),
                            html.Br(),
                            html.I(className='fas fa-long-arrow-alt-right'), 
                            " ",
                            html.Code("1,828,800 docking runs"),
                            "."
                        ],
                        className="card-text",
                    ),
                ]
            ),
            outline=True,
            className="w-80",
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H6(
                        [
                        html.Mark("3)"),
                        ' Docking performance per conformation'
                        ], 
                            className="card-title"),
                    html.Hr(style={'margin': '0'}),
                    html.P(
                        [
                            html.Code("AUC-ROC"),
                            ' as the virtual screening performance metric ',
                            html.I(className='fas fa-long-arrow-alt-right'),
                            ' ',
                            html.Code("AUC-ROC > 0.7"),
                            ' ',
                            html.Code("Druggable")
                        ],
                        className="card-text",
                    ),
                ]
            ),
            outline=True,
            className="w-80",
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H6(
                        [
                        html.Mark("4)"),
                        ' Protein binding site featurization'
                        ], 
                            className="card-title"),
                    html.Hr(style={'margin': '0'}),
                    html.P(
                        [
                            html.Code("POVME3"),
                            ' and ',
                            html.Code("AutoGrid"),
                            ' to evaluate the 3D properties of the binding site.',
                        ],
                        className="card-text",
                    ),
                ]
            ),
            outline=True,
            className="w-80",
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H6(
                        [
                        html.Mark("5)"),
                        ' 3D Convolutional Neural Network'
                        ], 
                            className="card-title"),
                    html.Hr(style={'margin': '0'}),
                    html.P(
                        [
                            html.I(className='fas fa-th'), ' ',
                            html.Code("X"), 
                            ': binding site features',
                            html.Br(),
                            html.I(className='fas fa-sort-numeric-up'), ' ',
                            html.Code("y"), 
                            ': conformation performance',
                            html.Br(),
                            html.I(className='fas fa-brain'),
                            html.Code("CNN"), 
                            ': ',
                            
                            html.Code("f(X)"),
                            html.I(className='fas fa-long-arrow-alt-right'),
                            html.Code("y"),
                        ],
                        className="card-text",
                    ),
                ]
            ),
            outline=True,
            className="w-80",
        ),
    ]
)


objective_col = dbc.Col(
    className='row-text-content',
    sm=12, lg=6,
    children=[
        html.H5(
            [
                'The objectives'
            ],
            className='h5-header'
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H6(
                        [
                        html.Mark("1)"),
                        ' Predictive model'
                        ], 
                            className="card-title"),
                    html.P(
                        [
                            'Build a ',
                            html.B('Machine Learning classifier'),
                            ' to predict which CDK2 conformation will ',
                            html.B('perform the best'),
                            ' in a virtual screening experiment.',
                           
                        ],
                        className="card-text",
                    ),
                ]
            ),
            outline=True,
            className="w-80",
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H6(
                        [
                        html.Mark("2)"),
                        ' Structural properties'
                        ], 
                            className="card-title"),
                    html.Hr(),        
                    html.P(
                        [
                            'Determine which ',
                           
                        ],
                        className="card-text",
                    ),
                ]
            ),
            outline=True,
            className="w-80",
        ),
    ]
)

# Molecule Viewer
mol_view_col = dbc.Col(
    lg=6,
    # className = 'plot-margin',
    children = [
        # dbc.Alert(
        #     [
        #         html.H4("Well done!", className="alert-heading"),
        #         html.P(
        #             "This is a success alert with loads of extra text in it. So much "
        #             "that you can see how spacing within an alert works with this "
        #             "kind of content."
        #         ),
        #         html.Hr(),
        #         html.P(
        #             "Let's put some more text down here, but remove the bottom margin",
        #             className="mb-0",
        #         ),
        #     ]
        # ),
        dbc.Container(
            id='viewport-crys-takeaway',
            children = [],
            style = {
                'width': '100%', 
                'minHeight': '420px',
                'overflow': 'hidden',
                'padding': '0',
                'margin': '0'
                }
            ),
        dbc.Alert(
            [
                html.H4([
                    html.Mark([
                        html.I(className="fas fa-american-sign-language-interpreting"),
                    ], className="alert-heading"),
                    " Interact !"
                    ]),
                    
                dcc.Markdown(
                    "This poster is aimed to be interactive." 
                ),
                html.Hr(),
                dcc.Markdown(
                    "For **more detailed explanations** about the methodology you can interact with some of the page elements."
                ),
            ],
            color = 'alert',
            dismissable=True,
        ),
    ]
)



# All Content
row_content = dbc.Row(
    children=[
        # Column 1
        summary_col,
        # # Column 2
        mol_view_col
    ]
)

col_contents = [
   row_titles,
   row_content 
]

app.clientside_callback(
    ClientsideFunction(
        namespace     = 'clientside',
        function_name = 'ngl_mol_cdk2_conf'
    ),
    Output('viewport-crys-takeaway', 'children'),
    Input('viewport-crys-takeaway',     'id')
    # Input('radioitems-conformations', 'value')
)