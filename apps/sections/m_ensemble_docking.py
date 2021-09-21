import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc


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
           lg=6, md=6, sm=12,
           children=[
             'ola'
           ]
       ),
       dbc.Col(
           lg=6, md=6, sm=12,
           children=[

           ]
           
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