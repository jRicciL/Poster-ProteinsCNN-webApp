import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc
from app import app

from dash.dependencies import Input, Output

# Titles
row_titles = dbc.Row(
    className='row-title-content',
    children= [
        # Title
       html.H2([
           "Convolutional Neural Networks",
           ]
           ),
       # Subtitle
       html.H3([
           'Exploring the implementation of CNN'
           ]
       )
    ]
)

# Col superior
upper_col_1 = dbc.Col(
    className='row-text-content',
    lg = 8, md=12,
    children=[
        html.P(
            [
            html.I(className='ico fas fa-chevron-right'),
            html.B(['A ', html.Mark('CNN binary classifier'), ' was implemented using Tenforflow and Keras:']),
            ],
        ),
        html.P(
            [
            html.I(className='ico fas fa-circle s2'),
            'The pocket voxelizations obtained with POVME 3 and AutoGrid were used as predicted variables.',
            ], className='ident-1'
        ),
        html.P(
            [
            html.I(className='ico fas fa-circle s2'),
            'The SBVS performance of each conformation was used as the target variable',
            ], className='ident-1'
        ),
        html.P(
           [
            html.I(className='ico fas fa-circle s2'),
            'Confs. with an AUC-ROC > 0.7 were labeled as "Druggable"'
           ], className='ident-1'
       ),
    ]
)


# Col superior
upper_col_2 = dbc.Col(
    className='row-text-content',
    lg = 4, md=12,
    children=[
        html.P(
            [
            html.I(className='ico fas fa-chevron-right'),
            'Different ',
            html.Mark('CNN architectures'),
            ' and voxelization types were evaluated. More details here: ',
            html.A(
                html.I(className='fab fa-github-alt'), 
                href='https://ebony-savory-246.notion.site/AutoGrid-and-CNNs-9f8722f576f84b759504d297424e161a',
                target='_blank')
            ],
            #
        ),
        html.P(
            [
            html.I(className='ico fas fa-chevron-right'),
            'More about the ',
            html.Mark('CNN implementation'),
            ' can be consulted here:',
            ' ',
            html.A(
                html.I(className='fab fa-github-alt'), 
                href='https://github.com/jRicciL/Poster-ProteinsCNN-webApp/blob/main/data/CNN_Autogrid_POVME_Classification_Poster_TEST.ipynb',
                target='_blank')
            ],
            #https://ebony-savory-246.notion.site/AutoGrid-and-CNNs-9f8722f576f84b759504d297424e161a
        ),

    ]
)


# All Content
upper_content = dbc.Row(
    children=[
        # Column 1
        upper_col_1,
        # Column 2
        upper_col_2 
    ]
)


# CardSlider column
col_card_slider = dbc.Col(
    lg = 8,
    children=[
        dbc.Carousel(
            items=[
                {"key": "1", "src": 
                    app.get_asset_url('images/POVME_AUTOGRID_cnn.png'),
                    'caption': 'Neural Network Architecture'},
                {"key": "2", "src": 
                    app.get_asset_url('images/POVME_AUTOGRID_cnn_training.png'),
                    'caption': 'Training performance'}, 
                {"key": "3", 
                "src": 
                    app.get_asset_url('images/POVME_AUTOGRID_cnn_test.png'),
                    'caption': 'Testing performance'
                },
            ],
            id='carousel',
            controls=False,
            interval=False,
            className='img-fluid carousel-cnn',
            indicators=False,
        ),
        dbc.RadioItems(
            id="slide-number",
            options=[
                {"label": "NN Architecture",      "value": 0},
                {"label": "Training performance", "value": 1},
                {"label": "Testing performance",  "value": 2},
            ],
            value=0,
            inline=True,
        ),
    ]
)

# Controls colum
col_controls = dbc.Col(
    lg=3, md = 12,
    children=[
        html.P(
            [
            html.I(className='ico fas fa-chevron-right'),
            'Use the ',
            html.B('Radio buttons'),
            ' below to select between four of the main results we obtained:',
            ],
        ),
         dbc.FormGroup(
                [
                html.Br(),
                dbc.Label(html.B("Select one assay to see the results:")),
                dbc.RadioItems(
                    options=[
                        {"label": "MLP + POVME", "value": 'POVME_mlp'},
                        {"label": "CNN + POVME", "value": 'POVME_cnn'},
                        {"label": "CNN + AUTOGRID", "value": 'AUTOGRID_cnn'},
                        {"label": "CNN + AUTOGRID + POVME", "value": 'POVME_AUTOGRID_cnn'},
                    ],
                    value='POVME_AUTOGRID_cnn',
                    id="radioitems-slider",
                ),
            ]
        )
    ]
)


# Lower content
lower_content = dbc.Row(
   children=[
        # Column 1
        col_controls,
        col_card_slider 
        # # Column 2
        # upper_col_2 
    ] 
)


col_contents = [
   row_titles,
   upper_content,
   html.Hr(),
   lower_content 
]

@app.callback(
    Output("carousel", "active_index"),
    Input("slide-number", "value"),
)
def select_slide(idx):
    return idx


@app.callback(
    [
     Output('carousel', 'items')
    ],
    [Input('radioitems-slider', 'value')]
)
def get_slider_data(value):
    slider_data =   [{"key": "1", "src": 
                    app.get_asset_url(f'images/{value}.png'),
                    'caption': 'Neural Network Architecture'},
                    {"key": "2", "src": 
                    app.get_asset_url(f'images/{value}_training.png'),}, 
                    {"key": "3", 
                    "src": 
                        app.get_asset_url(f'images/{value}_test.png'),
                    }]
    return [slider_data]