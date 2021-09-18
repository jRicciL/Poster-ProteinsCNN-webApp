import dash.html as html
import dash.dcc as dcc
from dash.html.I import I
import dash_bootstrap_components as dbc


# Titles
row_titles = dbc.Row(
    className='row-title-content',
    children= [
        # Title
       html.H2([
           'Protein Conformational Ensemble',
           ]
           ),
       # Subtitle
       html.H3([
           'Crystal Structures']
       )
    ]
)

# Descriptions and texts
row_texts = dbc.Col(
    className='row-text-content',
    children= [
        # Text
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            html.B('402'),
            ' crystallographic structures (conformations) of the CDK2 protein (',
            html.A(
                'P24941',
                href='https://www.uniprot.org/uniprot/P24941', target = '_blank'),
            ') were retrived from the ',
            html.A(
                'PDB', 
                href='https://www.rcsb.org/',
                target = '_blank'
                ),
            ' using the ',
            html.A(
                'ProDy', 
                href='http://prody.csb.pitt.edu/',
                target = '_blank'
                ),
            ' library.'
           ]
       ),
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            'The ',
            html.A(
                'Modeller', 
                href='https://salilab.org/modeller',
                target = '_blank'
                ),
            ' python module was used to ',
            html.B('model missing regions'),
            ' of the crystallographic conformations (',
            html.A(
                html.I(className='fab fa-github-alt'), 
                href='https://github.com/jRicciL/ML-ensemble-docking/blob/main/helper_modules/run_modeller.py',
                target = '_blank'
                ),
            ').'
           ]
       ),
    #    html.P(
    #        [
    #         html.I(className='ico fas fa-chevron-right'),
    #         html.A(
    #             'PDB2PQR', 
    #             href='https://pdb2pqr.readthedocs.io/en/latest/',
    #             target = 'blank'
    #             ),
    #         ' was used to fill missing heavy atoms, standardize residue names, and predict the protonation states of ionizable residues.'  
    #        ]
    #    ),
        html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            html.A(
                'Classical Multidimensional Scaling (cMDS)', 
                href='https://pdb2pqr.readthedocs.io/en/latest/',
                target = '_blank'
                ),
            " was performed using the pairwise ",
            html.B("RMSD"),
             " matrix calculated from the protein coordinates (",
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
            'The plot below shows the ',
            html.B('cMDS projection'),
            ' featuring the  ',
            html.Mark('Active', className='mark-red'),
            ' and ',
            html.Mark('Inactive', className='mark-grey'),
            ' states of the CDK2 protein (',
            html.A(),
            ').'
           ]
       )
    ]
)

row_content = dbc.Row(
    className= 'content-col-methods',
    children=[
        # Column 1
        dbc.Col(
            lg = 7,
            children=[
                row_texts,
                # Scatter plot cMDS
            ]
        ),
        # Column 2
        dbc.Col(
            lg = 3,
            children=[

            ]
        )
    ]
)

# Crystal structures content

col_container = dbc.Col(
    lg = 8, md = 12, sm = 12,
    className = 'col-container-methods',
    children = [
        row_titles,
        row_content,
        ],
)


