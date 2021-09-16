import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc

tab_introduction = dbc.Tab(
    label    = 'Introduction',
    children = [
        dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2],
                            'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5],
                         'type': 'bar', 'name': u'Montréal'},
                    ]
                }
            )
    ]
)