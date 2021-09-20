import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app
from apps.sections import m_flow
from apps.sections.m_cyto_elements import elements_labels
# Methods Section
from apps.sections import m_crys_structures
from apps.sections import m_conf_ensemble 
from apps.sections import m_pocket_featurization 
from apps.sections import m_md_structures
from apps.sections import m_ensemble_docking
from apps.sections import m_takeaway
from apps.sections import m_cnn 

# Second colum sections
sections_objs = [
    m_crys_structures.col_contents,
    m_md_structures.col_contents,
    m_conf_ensemble.col_contents,
    [],
    m_ensemble_docking.col_contents,
    m_pocket_featurization.col_contents,
    m_cnn.col_contents,
]
# ['Crystal Structures', 'MD Structures', 'Conf. Ensemble', 'Molecular Library', 'Ensemble Docking', 'Pocket Featurization', 'Convolutional Neural Network']

sections_dict = dict(zip(
   elements_labels,
   sections_objs
))


first_col_container = dbc.Col(
    lg = 4, md = 12, sm = 12,
    className = 'col-container-methods',
    children = m_flow.col_contents,
)

# Second column
# Requires a callback
second_col_container = dbc.Col(
    lg = 8, md = 12, sm = 12,
    id = 'col-container-methods',
    className = 'col-container-methods',
    children = []
)

# Main layout
layout = dbc.Row(
    className='section-container',
    children = [
       first_col_container,
       second_col_container
    ]
)

# Callback to update the second common
@app.callback(
    [
     Output('col-container-methods', 'children')
    ],
    [Input('cytoscape-methods', 'tapNodeData')]
    # [Input('reset-cytoscape', 'n_clicks')]
)
def displayTapNodeData(data):
    # default_label = 'Crystal Structures'
    default_label = 'MD Structures'
    if data == None:
        return [m_takeaway.col_contents]
        # return [m_cnn.col_contents]
    else:
        sec_name = data['label']

    if sec_name in elements_labels:
        if sec_name == 'Molecular Library':
            sec_name = 'Ensemble Docking'
        children = sections_dict[sec_name]
        # if sec_name == 'Ensemble Docking':
        #     return [m_takeaway.col_contents]
    else:
        children = m_takeaway.col_contents
    return [children]