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
    xs = 12, sm = 10, md = 8, lg = 10
)
logo_1 = dbc.Col([

    ],
    className = 'logo text-center',
    xs = 0, sm = 1, md = 2, lg = 1
)
logo_2 = dbc.Col([

    ],
    className = 'logo text-center',
    xs = 0, sm = 1, md = 2, lg = 1
)

# COMPONENT

layout = dbc.Row(
    [
        logo_1,
        title,
        logo_2,
    ],
    className = 'header'
)
