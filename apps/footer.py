import dash.html as html
import dash_bootstrap_components as dbc

#***********
# FOOTER
#***********
layout = html.Footer(
    [
        html.A(html.I(className='fab fa-github'),
        href='https://github.com/jRicciL',
        target='_blank'),
        '    ',
        html.A(html.I(className='fab fa-linkedin'),
        href='https://www.linkedin.com/in/joel-ricci-lopez/',
        target='_blank'),
        '    ',
        html.A(html.I(className='fab fa-twitter'),
        href='https://twitter.com/RicciBW',
        target='_blank'),
        ' ',
    ], 
    className='page-footer'
)