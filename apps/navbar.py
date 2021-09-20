from dash.html.Div import Div
from dash_bootstrap_components._components.Col import Col
from apps.sections import introduction
import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app


url_sections = {
    # 'Presentation'        : 'presentation',
    'Introduction'        : 'introduction',
    'Methods & Results'    : 'methods',
    # 'Results'             : 'results',
    'Conclusions'         : 'conclusions',
    # 'About'               : 'about'
}


layout = dbc.Row(
    className = 'navbar-container',
    children = [
        dbc.Col(
            
            sm =0, md = 0, lg = 2,
            
            ),
        dbc.Col(
            [
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink(
                            section_name,
                            href = f'/{section_url}',
                            id   = f'{section_url}-link' 
                        )) for section_name, section_url 
                                in url_sections.items()
                    ],
                    pills = True,
                    fill  = True, 
                    justified = True
                )
            ],
            md = 12, lg = 8
        ),
        dbc.Col(
            sm =0, md = 0, lg = 2)
    ],
)

@app.callback(
    [Output(f"{i}-link", "active") 
                    for i in url_sections.values()],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        active_links = [False for i in range(len(url_sections))]
        active_links[0] = True
        return active_links
    return [pathname == f'/{section_url}'
                for section_url in url_sections.values()]