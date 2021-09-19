import dash.html as html
import dash.dcc as dcc
from dash.html import Mark
from dash.html.I import I
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, ClientsideFunction
from app import app

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

list_of_four_confs = html.Ol(
    className='confs-list',
    children= [
        html.Li([
            html.Mark(
                html.A("1fin", href = 'https://www.rcsb.org/structure/1FIN', target='_black'),
                className='mark-confs mark-1fin'
            ),
                ": Active state"]),
        html.Li([
            html.Mark(
                html.A('4fku', href = 'https://www.rcsb.org/structure/4fku', target='_black'),
                className='mark-confs mark-4fku'
            ),
            ': Inactive ',
            html.Em('Src-like'),
            ' state']),
        html.Li([
            html.Mark(
                html.A('3pxf', href = 'https://www.rcsb.org/structure/3pxf', target='_black'),
                className='mark-confs mark-3pxf'
            ),
            ': Inactive ',
            html.Em('Open'),
            ' state']),
        html.Li([
            html.Mark(
                html.A('5a14', href = 'https://www.rcsb.org/structure/5a14', target='_black'),
                className='mark-confs mark-5a14'
            ),
            ': Inactive ',
            html.Em('DFG-out'),
            ' state']),
    ]
)

# Conformations radio items
confs_radioitems = dbc.FormGroup(
    [
        # dbc.Label("Choose one"),
        dbc.RadioItems(
            options=[
                {"label": "1fin: Active state", "value": 1},
                {"label": '4fku: Inactive "Src-like" state', "value": 2},
                {"label": '3pxf: Inactive "Open" state', "value": 3},
                {"label": '5A14: Inactive "DFG-out" state', "value": 4},
                ''
            ],
            value=1,
            inline=True,
            persistence=True,
            id="radioitems-input",
        ),
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
            html.B('402 crystallographic structures'),
            ' (conformations) of the CDK2 protein (',
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
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            html.A(
                'PDB2PQR', 
                href='https://pdb2pqr.readthedocs.io/en/latest/',
                target = 'blank'
                ),
            ' was used to predict the protonation states of ionizable residues.'  
           ]
       ),
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            html.B('Four representative'),
            ' PDB conformations were selected as the initial coordinates to perform ',
            html.B('Molecular Dynamics (MD)'),
            ' simulations.'
           ]
       ),
       list_of_four_confs, 
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            html.B('The properties'),
            ' of these conformational states have been described elsewhere.',
            html.Sup(
                [
                    html.A(1, href='https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0154066', target='_blank'),
                    ', ',
                    html.A(2, href='https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-017-1506-2', target='_blank'),
                ]
            ),
           ]
       ),
    #    html.P(
    #        [
    #         html.I(className='ico fas fa-chevron-right'),
    #         'These four structures were combined with three MD protocols to explore the conformational space of CDK2.'
    #        ]
    #    ),
    #     html.P(
    #        [
    #         html.I(className='ico fas fa-chevron-right'),
    #         html.A(
    #             'Classical Multidimensional Scaling (cMDS)', 
    #             href='https://en.wikipedia.org/wiki/Multidimensional_scaling#Classical_multidimensional_scaling',
    #             target = '_blank'
    #             ),
    #         " was performed using the pairwise ",
    #         html.B("RMSD"),
    #          " matrix calculated from atomic coordinates (",
    #         html.A(
    #             html.I(className='fab fa-github-alt'), 
    #             href='https://nbviewer.jupyter.org/github/jRicciL/CDK2_notebooks/blob/master/4_Trajectory_Analysis/3_Traj_projections.ipynb',
    #             target = '_blank'
    #             ),
    #         ').'  
    #        ]
    #    ),
    #    html.P(
    #        [
    #         html.I(className='ico fas fa-chevron-right'),
    #         'The plot below shows the ',
    #         html.B('cMDS projection'),
    #         ' featuring the  ',
    #         html.Mark('Active', className='mark-red'),
    #         ' and ',
    #         html.Mark('Inactive', className='mark-grey'),
    #         ' states of the CDK2 protein (',
    #         html.A('Pisani et al., 2016',
    #               href='https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0154066',
    #               target='_blank'),
    #         ').'
    #        ]
    #    )
    ]
)

# Conformations selection radiobutton
inline_radioitems = dbc.FormGroup(
    [
        dbc.RadioItems(
            options=[
                {"label": "1fin", "value": "1fin"},
                {"label": "4fku", "value": "4fku"},
                {"label": "3pxf", "value": "3pxf"},
                {"label": "5a14", "value": "5a14"},
            ],
            value="1fin",
            id="radioitems-conformations",
            inline=True,
            persistence=True,
            
        ),
    ]
)

checkbox_surface = dbc.FormGroup(

)

# Molecule Viewer
mol_view_col = dbc.Col(
    className = 'plot-margin mol-viewer',
    children = [
        dbc.Container(
            id='viewport-crys',
            children = [],
            style = {
                'width': '100%', 
                'minHeight': '515px',
                'overflow': 'hidden'
                # 'padding': '-3px',
                # 'margin': '0'
                }
            )
    ]
)


# All Content
row_content = dbc.Row(
    # className= 'content-col-methods',
    children=[
        # Column 1
        dbc.Col(
            lg = 6, md = 12,
            children=[
                row_texts,
            ]
        ),
        # Column 2
        dbc.Col(
            lg = 6, md = 12,
            children=[
                mol_view_col,
                inline_radioitems,
            ]
        )
    ]
)

# COL CONTENTS
col_contents = [
        row_titles,
        row_content
    ]

app.clientside_callback(
    ClientsideFunction(
        namespace     = 'clientside',
        function_name = 'ngl_mol_cdk2_conf'
    ),
    Output('viewport-crys', 'children'),
    Input('viewport-crys',     'id'),
    Input('radioitems-conformations', 'value')
)

