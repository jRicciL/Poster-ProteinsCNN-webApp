import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
from app import app

import plotly.graph_objects as go
from helpers.load_data import get_df_crys_prot
from helpers.load_data import get_df_md
from helpers.plotly_conf import plotly_conf
from helpers.mds_plot import get_mds_layout
from helpers.mds_plot import add_CRYS_mds_trace
from helpers.mds_plot import add_REFS_mds_trace 
from helpers.mds_plot import add_arrows_trace


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
ref_pdb_ids = ['1fin', '4fku', '3pxf', '5a14']
# Create the default figure
def get_default_mds_plot(
        atoms_subset = 'sec',
        ):
    df_prot_data = get_df_crys_prot()
    fig_mds = get_mds_layout()
    # CRYS
    fig_mds = add_CRYS_mds_trace(fig_mds, df_prot_data, 
         f'x_crys_{atoms_subset}', 
         f'y_crys_{atoms_subset}', 
         opacity=0.85)
    ref_pdb_ids = ['1fin', '4fku', '3pxf', '5a14']
    df_ref_confs = df_prot_data[df_prot_data['PDB-id'].isin(ref_pdb_ids)]
    fig_mds = add_REFS_mds_trace(fig_mds, 
                             df_ref_confs, 
                             f'x_crys_{atoms_subset}', 
                             f'y_crys_{atoms_subset}')

    return fig_mds 

# Create the user requested figure
def update_mds_plot(
        fig_mds_dict,
        atoms_subset = 'sec',
        switches_crys_ensembles_vals = [1, 0, 0], # Determine which crys draw
        switches_md_ensembles_vals = []
    ):
    df_prot_data = get_df_crys_prot()
    fig_mds = go.Figure(fig_mds_dict)
    fig_mds.data = []
    # CRYS
    fig_mds = add_CRYS_mds_trace(
                fig_mds, 
                df_prot_data, 
                f'x_crys_{atoms_subset}', 
                f'y_crys_{atoms_subset}', 
                opacity=0.85)
    # COnditional to the radio button 
    # CRYS MIN
    if 'min-crys' in switches_crys_ensembles_vals:
        fig_mds = add_CRYS_mds_trace(fig_mds, df_prot_data, 
            f'x_min_{atoms_subset}', 
            f'y_min_{atoms_subset}', 
            size_col='', single_size=2, 
            marker_symbol='triangle-up',
            hoverinfo='skip',
            size_scale=2.5,
            opacity=1,
            line_width=1,
            show_legend = False)
    
        if 'connects' in switches_crys_ensembles_vals: 
            fig_mds = add_arrows_trace(
                fig_mds, 
                df_prot_data, 
                f'x_crys_{atoms_subset}', 
                f'y_crys_{atoms_subset}',
                f'x_min_{atoms_subset}', 
                f'y_min_{atoms_subset}'
            )
    # Add MD conformations topology
    if len(switches_md_ensembles_vals) == 1:
        df_md = get_df_md() 
        fig_mds.add_trace(
            go.Histogram2dContour(
                x = df_md[f'x_dm_{atoms_subset}'],
                y = df_md[f'y_dm_{atoms_subset}'],
                hoverinfo='skip',
                showlegend=True,
                name = 'MD-confs.',
                autocontour = False,
                colorscale = 'Spectral_r',
                        ncontours = 25, histnorm = 'density',
                        showscale = False, line = {'width': 2},
                        contours = {'type': 'levels',  'coloring': 'lines'},
            )
        )

    # Always add the reference labels at the end
    ref_pdb_ids = ['1fin', '4fku', '3pxf', '5a14']
    df_ref_confs = df_prot_data[df_prot_data['PDB-id'].isin(ref_pdb_ids)]
    fig_mds = add_REFS_mds_trace(fig_mds, 
                             df_ref_confs, 
                             f'x_crys_{atoms_subset}', 
                             f'y_crys_{atoms_subset}')

    return fig_mds 

plot_subtitles = dbc.Row(
    className='row-title-content',
    children= [
       # Subtitle
       html.H3([
           'cMD projection: Crystal and MD structures']
       )
    ]
)
# Radio buttons to select protein substructure
radioitems_prot_section = dbc.FormGroup(
    [
        dbc.Label(html.B("CDK2 residues used:")),
        dbc.RadioItems(
            options=[
                {"label": "Secondary Structure residues", 
                 "value": 'sec'},
                {"label": "Pocket residues", 
                 "value": 'pkt'}
            ],
            value='sec',
            id="radioitems-prot-section",
        ),
    ]
)

# Protein Ensemble Groups
switches_crys_ensembles = dbc.FormGroup(
    [
        dbc.Label(html.B("CRYS conformations:")),
        dbc.Checklist(
            options=[
                {"label": "CRYS", "value": 'crys', "disabled": True},
                {"label": "MIN-CRYS", "value": 'min-crys'},
                {"label": "Show connections", 
                 "value": 'connects'},
            ],
            value=['crys'],
            id="switches-crys-ens",
            switch=True,
        ),
    ]
)

# MD Conformation topology plot
switches_md_ensembles = dbc.FormGroup(
    [
        dbc.Label(html.B("MD conformations:")),
        dbc.Checklist(
            options=[
                {"label": "MD conformations", "value": True},
            ],
            value=[],
            id="switches-md-ens",
            switch=True,
        ),
    ]
)

row_plot = dbc.Row(
    # className='row-text-content',
    children=[
        dbc.Col(
            lg=3, md=3, sm = 12,
            id='mds-ensemble-inputs',
            children=[
                radioitems_prot_section,
                switches_crys_ensembles,
                switches_md_ensembles 
            ]
        ),
        dbc.Col(
            lg=9, md=9, sm = 12,
            children=[
            dcc.Graph(
                id = 'mds-ensemble-plot',
                config = plotly_conf,
                figure = get_default_mds_plot() 
            ),
            ]
        )

    ]
    
)

col_contents = [
    row_titles,
    row_texts,
    plot_subtitles,
    row_plot 
]

# Render PLOT
@app.callback(
    [
        Output(component_id='mds-ensemble-plot',
               component_property='figure')
    ],
    [
        Input('mds-ensemble-plot', 'figure'),
        Input('radioitems-prot-section', 'value'),
        Input('switches-crys-ens', 'value'),
        Input('switches-md-ens', 'value'),
    ]
)
def render_mds_plot_methods(fig, 
            atoms_subset, 
            switches_crys_ensembles_vals,
            switches_md_ensembles_vals 
            ):
    new_fig = update_mds_plot(
            fig, 
            atoms_subset, 
            switches_crys_ensembles_vals,
            switches_md_ensembles_vals) 
    return [new_fig] 