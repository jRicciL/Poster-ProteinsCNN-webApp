import dash.html as html
import dash_bootstrap_components as dbc

#***********
# FOOTER
#***********
layout = html.Footer(
    [
        html.A('@Ricci-López',
        href='https://github.com/jRicciL',
        target='_blank')
    ], 
    className='page-footer'
)