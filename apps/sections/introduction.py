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
    #    html.Hr(),
    #    html.H2(
    #        html.Span([
    #        'Hola ',
    #         ' ',
    #         html.A('#LatinXChem2021', 
    #         href='https://twitter.com/hashtag/LatinXChem2021', 
    #         target = '_blank'),
    #         ' 🎉 🧬🧪'
    #        ])
    #        ),
        html.H2(
           html.Span([
           '¡Hola ',
            ' ',
            html.A('EMBO 2021', 
            href='https://meetings.embo.org/event/20-biomolecular-simulations', 
            target = '_blank'),
            ' 🧬🧪👾!'
           ]),
           style={'font-size': '1.6rem', 
                  'margin-top': '1.3rem',
                  'margin-bottom': '0.7rem',
                  },
           className='embo-title'
           ),
       # Subtitle
    #    html.Br(),
    #    html.A(html.Img(
    #     alt='LatinXchem logo',
    #     src=app.get_asset_url('images/latinchem_logo.png'),
    #     className='logo-img',
    #     ),
    #     href='https://www.latinxchem.org/', target='_blank'
    #    ),
    #    html.Hr()
    ]
)

text_content_col_1 = dbc.Col(
    className='row-text-content',
    lg = 4, md = 12, sm =12,
    children=[
        row_titles,
        # html.H3('Introduction'),
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.Col(
                        [
                            html.H5(
                                [
                                # html.I(className='fas fa-robot'),
                                " Briefly...",
                                ], 
                            className="card-title"), 
                        ], 
                    ),
                    dbc.Col(
                        [
                            dcc.Markdown(
                                [
                                    'We implemented a **convolutional neural network** classifier to predict **which CDK2 protein conformations** will perform **the best** in a *virtual screening* experiment.', 
                                ],
                                className="card-text",
                            ),
                            html.Img(
                                alt='LatinXchem logo',
                                src=app.get_asset_url('images/briefly.svg'),
                                className='img-fluid',
                            ),  
                        ], 
                       
                    ), 
                    
                ],
                className="card-brief-body",
            ),
            outline=True,
            className="card-brief",
        ),
        html.Br(),
        html.H4('Structure-based Virtual Screening (SBVS)'),
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                html.B(html.Mark('Molecular docking')),
                ' allows the evaluation of large numbers of small molecules to predict their interaction with a target protein.'
            ]
        ),
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                'Typical docking campaigns rely on a ',
                html.B('single rigid conformation'),
                ' of the target protein.'
            ]
        ),
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                'However, ',
                html.B('ignoring protein flexibility affects'),
                ' the accurate discrimination between true-binder and non-binder molecules.'
            ]
        ),
    ]
)


text_content_col_2  = dbc.Col(
    className='row-text-content',
    lg = 5, md = 12, sm =12,
    children=[
        # html.Img(
        #     alt='Virtual Screening',
        #     src=app.get_asset_url('images/virtual_screening.png'),
        #     className='img-fluid mt-2 p-4',
        # ),
        # html.Img(
        #     alt='Ensemble docking',
        #     src=app.get_asset_url('images/ensemble_docking.png'),
        #     className='img-fluid mt-2 p-4',
        # )
        
        html.Br(),
        html.H4('Ensemble-based Docking'),
        html.Br(),
        dbc.Carousel(
            items=[
                {"key": "1", "src": 
                    app.get_asset_url('images/virtual_screening.png')},
                {"key": "2", "src": 
                    app.get_asset_url('images/ensemble_docking.png')}, 
            ],
            id='carousel-intro',
            controls=True,
            # interval=True,
            className='carousel-intro',
            indicators=False,
        ),
        # html.H4('Ensemble-based Docking'),
        html.Hr(),
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                html.B(html.Mark('Ensemble docking (ED)', className='mark-blue')), ' incorporates protein flexibility during SBVS campaigns.'
            ]
        ), 
        html.P(
           [
           html.I(className='ico fas fa-chevron-right'), 
            'ED consists of ',
            html.B('docking the ligands'),
            ' to a set of ',
            html.B('different conformations'),
            ' of the target protein.'
           ], 
       ),
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            'ED has been ',
            html.B('successfully applied'),
            ' in several studies, but critical challenges still need to be addressed.'
           ],
       ),
    ]
)

text_content_col_3  = dbc.Col(
    className='row-text-content',
    lg = 3, md = 12, sm =12,
    children=[
        
    #    html.P(
    #        [
    #         html.I(className='ico fas fa-circle s2'),
    #         'However, critical challenges still need to be addressed.'
    #        ], className='ident-1'
    #    ),

    #    html.H4('But ... which conformations should we choose?'),
    html.Br(),
       html.H4(
           [
               html.Span('But, '),
               html.Span('how to select',
           className='intro-col3-title-mark'),
                html.Span(' the best ',
           className='intro-col3-title-mark'),
           html.Span('suitable ',
           className='intro-col3-title-mark'),
           html.Span('conformations?',
           className='intro-col3-title-mark'),
           ]
           ),
       html.P(
            [
                # html.I(className='ico fas fa-chevron-right'),
                html.Em('As of today there are no known metrics that can identify which protein structure will end up being selected by ligands.'),
                html.Br(),
                html.B(
                    [
                        html.I(className='fas fa-book'), ' ',
                        html.A('Evangelista, et al. (2019)',
                    href='https://pubs.acs.org/doi/10.1021/acs.jpcb.8b11491',
                    target='_blank'
                    )]
                )
            ], #className='text-right'
        ), 
        html.Hr(),
        html.P(
            [
                # html.I(className='ico fas fa-chevron-right'),
                html.Em('It remains difficult or impossible to know a priori which receptor conformations will result in an ensemble with virtual screening utility.'),
                html.Br(),
                html.B(
                    [
                        html.I(className='fas fa-book'), ' ',
                        html.A(' Swift, et al. (2016)',
                    href='https://pubs.acs.org/doi/10.1021/acs.jcim.5b00684',
                    target='_blank'
                    )]
                )
            ], #className='text-right'
        ), 
        html.Hr(),
        html.P(
            [
                # html.I(className='ico fas fa-chevron-right'),
                html.Em('Can we pick the best performing set a priori without evaluating the ability of each conformation to discriminate between known binders and nonbinders?'),
                html.Br(),
                html.B([
                    html.I(className='fas fa-book'), ' ',
                    html.A(' Rueda, et al. (2010)',
                    href='https://pubs.acs.org/doi/10.1021/ci9003943',
                    target='_blank'
                )]
                )
            ], #className='text-right'
        ), 
         html.H4('The CDK2 protein'),
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            'Here, we selected the ',
            html.Span(['cyclin-dependent kinase 2 (', html.Mark('CDK2'), ')']),
            ' protein  as a case study.'
           ],
       ), 
        html.P(
            [
                html.I(className='ico fas fa-circle s2'),
                'CDK2 has been widely employed to test and validate MD and SBVS methodologies.'
            ], 
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