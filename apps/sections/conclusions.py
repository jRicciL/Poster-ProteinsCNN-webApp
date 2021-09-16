import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app

layout = dbc.Tab(
    label    = 'Introduction',
    children = [
        html.H3('Conclusions placeholder'),
    ]
)