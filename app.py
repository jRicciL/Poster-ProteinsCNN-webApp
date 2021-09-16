import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


# Template
load_figure_template("journal")

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True, 
    meta_tags=[{'name': 'viewport',
                'content': 'width=device-width, initial-scale=1.0'
                }],
    external_stylesheets=[dbc.themes.JOURNAL]
)
app.title = 'JRL: LatinXChem poster'
server = app.server
