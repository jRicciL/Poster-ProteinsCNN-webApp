import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


# Template
load_figure_template("journal")

# External JS
external_scripts = [
    "https://unpkg.com/ngl@0.10.4/dist/ngl.js"
]

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True, 
    meta_tags=[{'name': 'viewport',
                'content': 'width=device-width, initial-scale=1.0'
                }],
    external_stylesheets=[dbc.themes.JOURNAL],
    external_scripts=external_scripts
)
app.title = 'JRL: LatinXChem poster'
server = app.server
