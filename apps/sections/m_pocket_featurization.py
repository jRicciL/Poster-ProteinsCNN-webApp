from dash.dcc.Markdown import Markdown
import dash.html as html
import dash.dcc as dcc
from dash.html.Mark import Mark
import dash_bootstrap_components as dbc

import plotly.graph_objects as go
from helpers.plotly_conf import plotly_conf
from helpers.load_data import get_plot_povme_tuple
from helpers.pocket_plot import plot_povme_pockets

from dash.dependencies import Input, Output

# Titles
row_titles = dbc.Row(
    className='row-title-content',
    children= [
        # Title
       html.H2([
           "Protein's Pocket Featurization",
           ]
           ),
       # Subtitle
       html.H3([
           'POVME and AutoGrid'
           ]
       )
    ]
)


# Text column
text_content_col = dbc.Col(
    className='row-text-content',
    lg = 5, md = 12,
    children=[
        html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            'The ',
            html.B('ATP binding site (pocket)'),
            ' of the CDK2 protein was evaluated using ',
            html.A('POVME3', href='https://pubs.acs.org/doi/abs/10.1021/acs.jctc.7b00500', target='_blank'),
            ' and ',
            html.A('AutoGrid 4', href='http://autodock.scripps.edu/wiki/AutoGrid', target='_blank'),
           ]
       ),
    #    html.P(
    #        [
    #         html.I(className='ico fas fa-chevron-right'),
    #         'The 1,524 conformations were aligned using the aC of the pocket residues.'
    #        ]
    #    ),
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            "POVME 3 was used to determine the shape and volume of each conformation's pocket."
           ],
       ),
       html.P(
           [
            html.I(className='ico fas fa-circle s1'),
            "Each pocket shape consisted of a cubic box:"
           ],
           className='ident-1'
       ),
        html.Ul(
           [
            html.Li(["With a ", html.Code("24x24x24 Å"), " size."]),
            html.Li("Comprising all pocket residues"),
            html.Li(["With ", html.Code("1.0 Å"), " spacing."]),
           ],
           className='ident-3'
       ),
       html.P(
           [
            html.I(className='ico fas fa-circle s1'),
            "The ",
            html.A("BINANA", href = 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3099006/'),
            " coloring scheme was used to identify five physicochemical properties."
           ],
           className='ident-1'
       ),
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            html.B("AutoGrid 4"),  
            " was used to calculate ", 
            html.Em("energy grid maps"), 
            " defining each pocket."
           ],
       ),
       html.P(
           [
            html.I(className='ico fas fa-circle s1'),
            "Each energy map consisted of a three-dimensional lattice where each voxel stores the energy of a 'probe' atom  regarding the protein atoms."
           ],
           className='ident-1'
       ),
       html.Ul(
           [
            html.Li("Three atom types ('A', 'HD', 'OA') maps"),
            html.Li("An electrostatic ('e') map"),
            html.Li("A desolvation ('d') map."),
           ], 
           className='ident-3'
       ),
       html.P(
           [
            html.I(className='ico fas fa-circle s1'),
            "The spacing, center and size of the grid box was the same as POVME's."
           ],
           className='ident-1'
       ),
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            html.Mark("The 3D plot"), " shows the ", html.B("pocket voxelization"), " as defined by POVME and AutoGrid."
           ],
       ),
    ]
)

def plot_povme():
    X, prot_centered, label_confs, label_channels, _, _ = get_plot_povme_tuple()
    fig = plot_povme_pockets(X, 
                             prot_centered, 
                             label_confs, 
                             label_channels)
    return fig

# 3D plot
plot_content_col = dbc.Col(
    lg = 7, md = 12,
    children=[
        dcc.Loading(
                    id="loading-2",
                    children=[dcc.Graph(
                                id = 'pocket-3d-plot',
                                config = plotly_conf,
                                figure = plot_povme() 
                                ),],
                    type="circle",
                )
        
    ]
)

# All Content
row_content = dbc.Row(
    children=[
        # Column 1
        text_content_col,
        # Column 2
        plot_content_col 
    ]
)


col_contents = [
   row_titles,
   row_content 
]
