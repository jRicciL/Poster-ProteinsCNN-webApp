from types import LambdaType
import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app
# Header and Footer components
from apps import header
from apps import footer
from apps import navbar
# Content components
from apps.sections import conclusions, introduction, methods


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    header.layout,
    navbar.layout,
    html.Div(id='page-content'),
    footer.layout
])


# Callback
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
    )
def display_page(pathname):
    if   pathname == '/':
        return introduction.layout
    elif pathname == '/introduction':
        return introduction.layout 
    elif pathname == '/methods':
        return methods.layout
    elif pathname == '/conclusions':
        return conclusions.layout
    else:
        return html.H1("404: Not found", className="text-danger")


if __name__ == '__main__':
    app.run_server(debug=True)