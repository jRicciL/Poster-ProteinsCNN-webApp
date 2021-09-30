import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc

from app import app

# Titles
row_titles = dbc.Row(
    className='row-title-content',
    children= [
        # Title
       html.H2([
           "Ensemble-based Docking",
           ]
           ),
       # Subtitle
       html.H3([
           'Individual performance of each protein conformation'
           ]
       )
    ]
)

# Text content
row_texts = dbc.Row(
    className='row-text-content',
    children= [
       dbc.Col(
           lg=12, md=12, sm=12,
           children=[
             html.P(
                [
                    html.I(className='ico fas fa-circle s2'),
                    html.Mark("AUC-ROC"),
                    ' was used to evaluate the ',
                    html.B('docking performance'),
                    ' of ',
                    html.Mark('each conformation.'),
                ], #className='ident-1'
            ),
           html.P(
                [
                    html.I(className='ico fas fa-circle s2'),
                    'Conformations with ',
                    html.Code(html.Mark('AUC ROC > 0.7')),
                    ' were labeled as ',
                    html.Mark('"Druggable"', className='pill pill-red')
                ], className='ident-1'
            ),
           ]
       ),
       dbc.Col(
           lg=12, md=12, sm=12,
           children=[
               html.Hr(),
               html.Br(),
               html.H5(
                   [
                    'AUC-ROC:',
                    html.Span(' SBVS performance per conformation',
                        style={'font-weight': '300'}
                    ),
                   ]
                ),
               html.Img(
                alt='SBVS AUC-ROC per conformation',
                src=app.get_asset_url('images/auc_roc_per_conformation.png'),
                className='img-fluid max-width mx-auto',
            )
           ], className='text-center'
           
       )
    ]
)



# All Content
# row_content = dbc.Row(
#     children=[
#         # Column 1
#         text_content_col_1,
#         # # Column 2
#         # text_content_col_2 
#     ]
# )


col_contents = [
   row_titles,
   row_texts 
]