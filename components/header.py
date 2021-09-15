import dash.html as html
import dash_bootstrap_components as dbc

#***********
# HEADER
#***********
text_title = 'Druggability prediction of protein conformations using convolutional neural networks'
title = dbc.Col([
        html.H1(text_title, className='h1')
    ], 
    className='title text-center',
    sm = 12, md = 8, lg = 8
)
logo_1 = dbc.Col([

    ],
    className='logo text-center',
    sm = 0, md = 2
)
logo_2 = dbc.Col([

    ],
    className='logo text-center',
    sm = 0, md = 2
)

header = dbc.Row(
    [
        logo_1,
        title,
        logo_2,
    ],
)
