import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app


text_content_col_1  = dbc.Col(
    className='row-text-content',
    lg = 4, md = 12, sm =12,
    children=[
       html.H3('Conclusions'),
       html.Hr(),
       html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                'A set of ', 
                html.B('60,000 conformations'),
                ' of CDK2 were generated using different MD protocols.'
            ]
        ),
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                'Conformations ',
                html.B('structurally similar'),
                html.Mark(html.B((' do not ')),
                html.B('necessarily have a '),
                'similar SBVS performance.'
            ]
        ),
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                'A CNN binary classifier was implemented using POVME and AutoGrid voxelizations to predict the SBVS performance of each CDK2 conformation.'
            ]
        ),
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                html.B("The CNN with the best performance:")
            ], 
        ),
        html.P(
            [
                html.I(className='ico fas fa-circle s2'),
                html.Mark('POVME', className='pill pill-blue'), 
                '+', 
                html.Mark('AutoGrid',  className='pill pill-red'),
            ], className='ident-1'
        ),
        html.P(
            [
                html.I(className='ico fas fa-circle s2'),
                html.B("Validation"), " set: ", html.Code("0.83 AUC-ROC"),
            ], className='ident-2'
        ),
        html.P(
            [
                html.I(className='ico fas fa-circle s2'),
                html.B("Testing"), " set: ", html.Code("0.87 AUC-ROC"),
            ], className='ident-2'
        ),
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                'The results obtained with the CNN model confirm that the shape and the physicochemical properties of a given CDK2 conformation can be used to determine its utility in a Ensemble docking campaign.'
            ]
        ),
    ]
)

text_content_col_2  = dbc.Col(
    className='row-text-content',
    lg = 4, md = 12, sm =12,
    children=[
        html.H3('Limitations and perspectives'),
        html.Hr(),
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                'This has been just an exploratory analysis and there are still many limitations:'
            ]
        ),
        html.P(
            [
                html.I(className='ico fas fa-circle s2'),
                'The dataset was relatively limited with only 1,524 conformations.'
            ], className='ident-1'
        ),
        html.P(
            [
                html.I(className='ico fas fa-circle s2'),
                "Enhancing sampling MD methods could be used to enrich the conformational ensamble."
            ], className='ident-1'
        ),
         html.P(
            [
                html.I(className='ico fas fa-circle s2'),
                'We followed a classification approach, a regression model could be more suitable for this study.'
            ], className='ident-1'
        ),
        # html.P(
        #     [
        #         html.I(className='ico fas fa-circle s2'),
        #         "There are still many hyperparameters to test and evaluate in order to improve the ML model's performance."
        #     ], className='ident-1'
        # ),
        html.P(
            [
                html.I(className='ico fas fa-circle s2'),
                "There are still many hyperparameters to test and evaluate in order to improve the ML model's performance."
            ], className='ident-1'
        ), 
        html.P(
            [
                html.I(className='ico fas fa-circle s2'),
                "Some approaches such Grad-CAM can be used to enhance the explainability of the CNN models."
            ], className='ident-1'
        ),  
        
    ]
)

text_content_col_3  = dbc.Col(
    className='row-text-content text-align-center',
    lg = 4, md = 12, sm =12,
    children=[
        html.H3('Acknowledgements'),
        html.Hr(),
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                'The #LatinXChem community: organizers and attendees.'
            ]
        ), 
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                'My advisors:'
            ]
        ),
        html.P(
            [
                html.I(className='ico fas fa-circle s2'),
                "Professor Carlos A. Brizuela, CICESE, México."
            ], className='ident-1'
        ),
        html.P(
            [
                html.I(className='ico fas fa-circle s2'),
                "Professor Sergio A. Aguila, CNyN, UNAM, México."
            ], className='ident-1'
        ),
        html.P(
            [
                html.I(className='ico fas fa-circle s2'),
                "Professor Marcelino Arciniega, IFC, UNAM, México"
            ], className='ident-1'
        ),
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                'To all developers and researchers who have provided us with excellent tools and knowledge to carry out our research.'
            ]
        ), 
        html.P(
            [
                html.I(className='ico fas fa-chevron-right'),
                'Web application available thanks to:',
                html.A('Python',
                    href='https://www.python.org/',
                    target='_blank'
                ), ', ',
                html.A('Dash/Plotly',
                    href='https://dash.plotly.com',
                    target='_blank'
                ), ', ',
                html.A('Heroku',
                    href='https://www.heroku.com',
                    target='_blank'
                ), ', ',
                html.A('Google (Colab/Keras/Tensorflow)',
                    href='https://www.tensorflow.org/',
                    target='_blank'
                ), '.'
            ]
        ), 
    ]
)


thanks_row = dbc.Col([
        html.A(html.Img(
        alt='LatinXchem logo',
        src=app.get_asset_url('images/latinchem_logo.png'),
        className='logo-img',
        ),
        href='https://www.latinxchem.org/', target='_blank'
       ), 
        html.H3(
           html.Span([
           'Gracias ',
            ' ',
            html.A('#LatinXChem2021', 
            href='https://twitter.com/hashtag/LatinXChem2021', 
            target = '_blank'),
           ])
        ),
        
        html.Hr()
    ], lg = 12, style={'margin-top': '60px'},
    className='row-text-content text-center',)



layout = dbc.Row(
        className='section-container',
        children = [
        text_content_col_1,
        text_content_col_2,
        text_content_col_3,
        thanks_row 
        ]
    ) 
