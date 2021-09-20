import dash.html as html
import dash_bootstrap_components as dbc
from app import app

#***********
# HEADER
#***********
text_title = 'Druggability prediction of protein conformations using convolutional neural networks'
authors_text = [html.A('Joel Ricci-López', href = 'https://twitter.com/RicciBW', target='_blank'), ', ',
                html.A('Sergio. A. Águila', href='https://aguilalab.com/sergio-aguila', target='_blank'),  ', ',
                html.A('Carlos A. Brizuela', href='https://www.cicese.edu.mx/investigacion/personal_academico/913', target='_blank')]

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
        html.A(html.Img(
        alt='CICESE logo',
        src=app.get_asset_url('images/cicese_logo.png'),
        className='logo-img logo-left',
        ), href='https://www.cicese.edu.mx/', target='_blank')
    ],
    className = 'logo text-center',
    xs = 0, sm = 1, md = 2, lg = 1
)
logo_2 = dbc.Col([
        html.A(html.Img(
        alt='CNyN logo',
        src=app.get_asset_url('images/cnyn_logo.png'),
        className='logo-img logo-right',
        ),
        href='https://www.cnyn.unam.mx/', target='_blank'
        )
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
