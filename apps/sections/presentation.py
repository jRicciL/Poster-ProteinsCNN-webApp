import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app


# Titles
row_titles = dbc.Row(
    className='row-title-content',
    children= [
        # Title
       html.H2([
           "Molecular Dynamics Structures",
           ]
           ),
       # Subtitle
       html.H3([
           'Generation of MD-derived structures'
           ]
       )
    ]
)



layout = dbc.Row(
    className='section-container',
    children = [
      row_titles 
    ]
)