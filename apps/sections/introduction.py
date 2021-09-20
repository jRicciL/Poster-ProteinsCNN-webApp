import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, ClientsideFunction

import dash_defer_js_import as dji

from app import app



# Titles
row_titles = dbc.Col(
    lg=12,
    className='row-title-content logo text-center',
    children= [
        # Title
       html.Hr(),
       html.H2(
           html.Span([
           'Hola ',
            ' ',
            html.A('#LatinXChem2021', 
            href='https://twitter.com/hashtag/LatinXChem2021', 
            target = '_blank'),
           ])
           ),
       # Subtitle
       html.Br(),
       html.Img(
        alt='LatinXchem logo',
        src=app.get_asset_url('images/latinchem_logo.png'),
        className='logo-img',
        ),
       html.Hr()
    ]
)

text_content_col_1 = dbc.Col(
    className='row-text-content',
    lg = 4, md = 12, sm =12,
    children=[
        row_titles,
        html.H3('Introduction'),
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.Col(
                        [
                            html.H5(
                                [
                                "Briefly...",
                                ], 
                            className="card-title"), 
                        ], 
                    ),
                    dbc.Col(
                        [
                            dcc.Markdown(
                                [
                                    'We implemented a machine learning  model  to predict **which protein conformations** will perform **the best** in a *virtual screening* experiment.'
                                ],
                                className="card-text",
                            ),
                        ], 
                       
                    ), 
                    
                ]
            ),
            outline=True,
            # className="w-80",
        ),
        html.H4('Structure-based Virtual Screening (SBVS)'),
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                'Molecular docking allows the evaluation of large numbers of small molecules to predict their interaction with a target protein.'
            ]
        ),
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                'Typical docking campaigns rely on a single rigid conformation of the target protein.'
            ]
        ),
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                'However, ignoring protein flexibility affects the accurate discrimination between true-binder and non-binder molecules.'
            ]
        ),
    ]
)


text_content_col_2  = dbc.Col(
    className='row-text-content',
    lg = 5, md = 12, sm =12,
    children=[
        html.Img(
            alt='Virtual Screening',
            src=app.get_asset_url('images/virtual_screening.png'),
            className='img-fluid mt-2 p-4',
        ),
        html.Img(
            alt='Ensemble docking',
            src=app.get_asset_url('images/ensemble_docking.png'),
            className='img-fluid mt-2 p-4',
        )
    ]
)

text_content_col_3  = dbc.Col(
    className='row-text-content',
    lg = 3, md = 12, sm =12,
    children=[
        html.H4('Ensemble-based Docking'),
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                'Ensemble docking (ED) incorporates protein flexibility during SBVS campaigns.'
            ]
        ), 
        html.P(
           [
            html.I(className='ico fas fa-circle s2'),
            'ED consists of docking the ligands to a set of different conformations of the target protein.'
           ], className='ident-1'
       ),
       html.P(
           [
            html.I(className='ico fas fa-circle s2'),
            'ED has been successfully applied in several studies, but critical challenges still need to be addressed.'
           ], className='ident-1'
       ),
    #    html.P(
    #        [
    #         html.I(className='ico fas fa-circle s2'),
    #         'However, critical challenges still need to be addressed.'
    #        ], className='ident-1'
    #    ),

    #    html.H4('But ... which conformations should we choose?'),
       html.H4('But, how to select the best suitable conformations?'),
       html.P(
            [
                # html.I(className='ico fas fa-chevron-right'),
                html.Em('As of today there are no known metrics that can identify which protein structure will end up being selected by ligands.'),
                html.Br(),
                html.B(html.A('Evangelista, et al. (2019)'))
            ], className='text-right'
        ), 
        html.Hr(),
        html.P(
            [
                # html.I(className='ico fas fa-chevron-right'),
                html.Em('It remains difficult or impossible to know a priori which receptor conformations will result in an ensemble with virtual screening utility.'),
                html.Br(),
                html.B(html.A('Swift, et al. (2016)'))
            ], className='text-right'
        ), 
        html.Hr(),
        html.P(
            [
                # html.I(className='ico fas fa-chevron-right'),
                html.Em('Can we pick the best performing set a priori without evaluating the ability of each conformation to discriminate between known binders and nonbinders?'),
                html.Br(),
                html.B(html.A('Rueda, et al. (2010)'))
            ], className='text-right'
        ), 
    ]
)


layout = dbc.Row(
    className='section-container',
    children = [
    #   row_titles,
      text_content_col_1,
      text_content_col_2,
      text_content_col_3,
    ]
)