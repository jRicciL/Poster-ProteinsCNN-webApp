import dash.html as html
import dash.dcc as dcc
from dash.html import Mark
from dash.html.I import I
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, ClientsideFunction
from app import app

from helpers.load_data import get_df_crys_prot
from helpers.plotly_conf import plotly_conf
from helpers.mds_plot import get_mds_layout
from helpers.mds_plot import add_CRYS_mds_trace
from helpers.mds_plot import add_REFS_mds_trace 


# Titles
row_titles = dbc.Row(
    className='row-title-content',
    children= [
        # Title
       html.H2([
           'Conformational Ensemble',
           ]
           ),
       # Subtitle
       html.H3([
           'Crystal Structures + MD structures']
       )
    ]
)

# List of conf ensembles
list_of_conf_ensembles = html.Ul(
    className='ensembles-list',
    children = [
        html.Li([
            html.Mark(
                html.B('CRYS'),
                className=''
            ),
            ': 402 crystal structures.'
        ]),
        html.Li([
            html.Mark(
                html.B('MIN-CRYS'),
                className=''
            ),
            ': 402 CRYS after energy minimization.'
        ]),
        html.Li([
            html.Mark(
                html.B('MD'),
                className=''
            ),
            ': 360 MD-derived structures.'
        ]),
        html.Li([
            html.Mark(
                html.B('MIN-MD'),
                className=''
            ),
            ': 360 MD after energy minimization.'
        ]),
    ]

)

# Text content
row_texts = dbc.Row(
    className='row-text-content',
    children= [
       dbc.Col(
           lg=6, md=6, sm=12,
           children=[
               html.P(
                    [
                    html.I(className='ico fas fa-chevron-right'),
                    'The protein ',
                    html.B('conformational ensemble')
                    ,
                    ' comprised ',
                    html.B('1,524'),
                    ' structures:',
                    ],
                ),
                list_of_conf_ensembles
           ]
       ),
       dbc.Col(
           lg=6, md=6, sm=12,
           children=[
                html.P(
                [
                html.I(className='ico fas fa-chevron-right'),
                html.B('Classical Multidimensional Scaling'),
                ' (',
                html.A(
                    'cMDS', 
                    href='https://en.wikipedia.org/wiki/Multidimensional_scaling#Classical_multidimensional_scaling',
                    target = '_blank'
                    ),
                ") was performed using the pairwise ",
                html.B("RMSD"),
                " matrix calculated from the protein's atomic coordinates (",
                html.A(
                    html.I(className='fab fa-github-alt'), 
                    href='https://nbviewer.jupyter.org/github/jRicciL/CDK2_notebooks/blob/master/4_Trajectory_Analysis/3_Traj_projections.ipynb',
                    target = '_blank'
                    ),
                ').'  
                ]
            ),
            html.P(
                [
                    html.I(className='ico fas fa-chevron-right'),
                    'The ',
                    html.B('plot below'), 
                    ' shows the ',
                    html.B('projection'),
                    ' of the MD conformations over the ',
                    html.B('cMDS subspace'),
                    ' defined by the crystallographic structures (',
                    html.A('Pisani et al., 2016',
                        href='https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0154066',
                        target='_blank'),
                    ').'
                ]
            )
           ]
           
       )
    ]
)

# Plot Row

# Create the default figure
def get_def_mds_plot(atoms_subset = 'sec'):
    df_prot_data = get_df_crys_prot()
    fig_mds = get_mds_layout()
    # CRYS
    fig_mds = add_CRYS_mds_trace(fig_mds, df_prot_data, 
         f'x_crys_{atoms_subset}', 
         f'y_crys_{atoms_subset}', 
         opacity=0.85)
    # CRYS MIN
    # fig_mds = add_CRYS_mds_trace(fig_mds, df_prot_data, 
    #       f'x_min_{atoms_subset}', 
    #       f'y_min_{atoms_subset}', 
    #       size_col='', single_size=2, 
    #       marker_symbol='triangle-up',
    #       hoverinfo='skip',
    #       size_scale=2.5,
    #       show_legend = False)
    return fig_mds 

row_plot = dbc.Row(
    # className='row-text-content',
    children=[
        dbc.Col(
        lg=3, md=4, sm = 12,
        id='mds-ensemble-inputs',
        ),
        dbc.Col(
            lg=9, md=8, sm = 12,
            children=[
            dcc.Graph(
                id = 'mds-ensemble-plot',
                config = plotly_conf,
                figure = get_def_mds_plot() 
            ),
            ]
        )

    ]
    
)


col_contents = [
    row_titles,
    row_texts,
    row_plot 
]

# Render PLOT
