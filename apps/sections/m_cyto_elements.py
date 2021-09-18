
x = 170
y = 60

def get_cyto_elements():
    elements = [
        # The nodes elements
            # Parent Nodes
            {
                'data': {'id': 'ProtPrep', 
                'label': 'Protein Conformational Ensemble'},
                'position': {'x': x, 'y': y},
                'grabbable': True,
                'selectable': False,
                'locked': False
            },
            {
                'data': {'id': 'Crys', 
                'label': 'Crystal Structures',
                'parent': 'ProtPrep'},
                'selected': True,
                'grabbable': False,
                'selectable': True
            },
            {
                'data': {'id': 'MD', 
                'label': 'MD Structures',
                'parent': 'ProtPrep'},
                'grabbable': False,
                'selectable': True
            },
            {
                'data': {'id': 'ConfEns', 
                'label': 'Conf. Ensemble',
                'parent': 'ProtPrep'},
                'grabbable': False,
                'selectable': True
            },
            {
                'data': {'id': 'MolLib', 
                'label': 'Molecular Library'},
                'grabbable': True,
                'locked': False
            },
            {
                'data': {'id': 'EnsDock', 
                'label': 'Ensemble Docking'}
            },
            {
                'data': {'id': 'Features', 
                'label': 'Pocket Featurization'}
            },
            {
                'data': {'id': 'CNN', 
                'label': 'Convolutional Neural Network'}
            },

            # Children nodes
            {
                'data': {'id': 'one', 
                        'label': 'PDB Structures',
                        'parent': 'Crys'},
                'position': {'x': x, 'y': y},
                # 'locked': True,
                'grabbable': False,
                'selectable': False
            },
            {
                'data': {'id': 'two', 
                        'label': 'Structure Modeling',
                        'parent': 'Crys'},
                'position': {'x': x, 'y': y*2},
                # 'locked': True,
                'grabbable': False,
                'selectable': False
            },
            {
                'data': {'id': 'three', 
                        'label': 'Molecular Dynamics',
                        'parent': 'MD'},
                'position': {'x': x*2, 'y': y*2},
                # 'locked': True,
                'grabbable': False,
                'selectable': False
            },
            {
                'data': {'id': 'four', 
                        'label': 'Clustering',
                        'parent': 'MD'},
                'position': {'x': x*2, 'y': y*3},
                # 'locked': True,
                'grabbable': False,
                'selectable': False
            },
            {
                'data': {'id': 'five', 
                        'label': '1,524 structures',
                        'parent': 'ConfEns'},
                'position': {'x': x*1.5, 'y': y*4.5},
                # 'locked': True,
                'grabbable': False,
                'selectable': False
            },
            {
                'data': {'id': 'six', 
                    'label': 'DEKOIS 2.0',
                    'parent': 'MolLib'},
                'position': {'x': x*3, 'y': y*4.5},
                # 'locked': True,
                'grabbable': False,
                'selectable': False
            },
            {
                'data': {'id': 'seven', 'label': 'Docking Performance', 'parent': 'EnsDock'},
                'position': {'x': x*2.25, 'y': y*6.5},
                # 'locked': True,
                'grabbable': False,
                'selectable': False
            },
            {
                'data': {'id': 'eight', 
                        'label': 'POVME',
                        'parent': 'Features'},
                'position': {'x': x*0.75, 'y': y*6.5},
                # 'locked': True,
                'grabbable': False,
                'selectable': False
            },
            {
                'data': {'id': 'nine', 
                        'label': 'AutoGrid',
                        'parent': 'Features'},
                'position': {'x': x*1.25, 'y': y*6.5},
                # 'locked': True,
                'grabbable': False,
                'selectable': False
            },
            {
                'data': {'id': 'ten', 
                        'label': 'X: Predictive Var.',
                        'parent': 'CNN'},
                'position': {'x': x*1, 'y': y*8.25},
                # 'locked': True,
                'grabbable': False,
                'selectable': False
            },
            {
                'data': {'id': 'elev', 
                        'label': 'y: Response Var.',
                        'parent': 'CNN'},
                'position': {'x': x*2, 'y': y*8.25},
                # 'locked': True,
                'grabbable': False,
                'selectable': False
            },
            {
                'data': {'id': 'twelve', 
                        'label': 'CNN: f(X) ~ y',
                        'parent': 'CNN'},
                'position': {'x': x*1.5, 'y': y*9.5},
                # 'locked': False,
                'grabbable': False,
                'selectable': False
            },


            # Targets
            {'data': {'source': 'one', 'target': 'two'},
                'selectable': False},
            {'data': {'source': 'two', 'target': 'five'},
                'selectable': False},
            {'data': {'source': 'two', 'target': 'three'},
                'selectable': False},
            {'data': {'source': 'three', 'target': 'four'},
                'selectable': False},
            {'data': {'source': 'four', 'target': 'five'},
                'selectable': False},
            {'data': {'source': 'five', 'target': 'seven'},
                'selectable': False}, 
            {'data': {'source': 'six', 'target': 'seven'},
                'selectable': False}, 
    ]
    return elements

main_elements = get_cyto_elements()[1:8]
elements_labels = [e['data']['label'] 
                    for e in main_elements]