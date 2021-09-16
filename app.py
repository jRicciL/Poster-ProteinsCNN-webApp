import os
import dash
import dash.dcc as dcc
import dash.html as html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from dash.exceptions import PreventUpdate

import plotly.express as px
import pandas as pd
# Components
from components.header import header
from components.footer import footer
from components.sections_tabs import sections_tabs

# Template
load_figure_template("journal")

app = dash.Dash(
    __name__, 
    external_stylesheets=[dbc.themes.JOURNAL]
)
app.title = 'JRL: LatinXChem poster'



#***********
# CONTENT
#***********
# PDB examples


#***********
# APP LAYOUT
#***********
app.layout = dbc.Container(
    [
        header,
        sections_tabs,
        footer
    ],
    fluid = True,
)



if __name__ == '__main__':
    app.run_server(debug=True)