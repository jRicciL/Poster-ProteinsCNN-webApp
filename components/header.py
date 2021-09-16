import dash.html as html
import dash_bootstrap_components as dbc

#***********
# HEADER
#***********
text_title = 'Druggability prediction of protein conformations using convolutional neural networks'
authors_text = 'Joel Ricci-López, Sergio. A. Águila, Carlos A. Brizuela'

title = dbc.Col([
        html.H1(text_title, 
                className='title-text'),
        html.P(authors_text,
                className='authors-text'),
    ], 
    className = 'title-col text-center',
    sm = 12, md = 8, lg = 8
)
logo_1 = dbc.Col([

    ],
    className = 'logo text-center',
    sm = 0, md = 2
)
logo_2 = dbc.Col([

    ],
    className = 'logo text-center',
    sm = 0, md = 2
)

# COMPONENT

header = dbc.Row(
    [
        logo_1,
        title,
        logo_2,
    ],
    className = 'header'
)
