import dash.html as html
import dash_bootstrap_components as dbc
# Import each tab module
from components.tabs.tab_introduction import tab_introduction

sections_tabs = html.Div(
    [
        dbc.Tabs(
            [
            tab_introduction 
            ],
        )
    ],
    className = 'tabs-content',
)
