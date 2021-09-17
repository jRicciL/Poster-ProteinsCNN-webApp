
x = 170
y = 60

elements = [
    # The nodes elements
        # Parent Nodes
        {
            'data': {'id': 'ProtPrep', 
            'label': 'Protein Preparation'}
        },
        {
            'data': {'id': 'Crys', 
            'label': 'Crystal Structures',
            'parent': 'ProtPrep'}
        },
        {
            'data': {'id': 'MD', 
            'label': 'MD Structures',
            'parent': 'ProtPrep'}
        },
        {
            'data': {'id': 'ConfEns', 
            'label': 'Conf. Ensemble',
            'parent': 'ProtPrep'}
        },
        {
            'data': {'id': 'MolLib', 
            'label': 'Molecular Library'}
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
            'locked': True
        },
        {
            'data': {'id': 'two', 
                     'label': 'Structure Modeling',
                     'parent': 'Crys'},
            'position': {'x': x, 'y': y*2},
            'locked': True
        },
        {
            'data': {'id': 'three', 
                     'label': 'Molecular Dynamics',
                     'parent': 'MD'},
            'position': {'x': x*2, 'y': y*2},
            'locked': True
        },
        {
            'data': {'id': 'four', 
                      'label': 'Clustering',
                     'parent': 'MD'},
            'position': {'x': x*2, 'y': y*3},
            'locked': True
        },
        {
            'data': {'id': 'five', 
                     'label': '1,524 structures',
                     'parent': 'ConfEns'},
            'position': {'x': x*1.5, 'y': y*4.5},
            'locked': True
        },
        {
            'data': {'id': 'six', 
                'label': 'DEKOIS 2.0',
                'parent': 'MolLib'},
            'position': {'x': x*3, 'y': y*4.5},
            'locked': True
        },
        {
            'data': {'id': 'seven', 'label': 'Docking Performance', 'parent': 'EnsDock'},
            'position': {'x': x*2.25, 'y': y*6.5},
            'locked': True
        },
        {
            'data': {'id': 'eight', 
                     'label': 'POVME',
                     'parent': 'Features'},
            'position': {'x': x*0.75, 'y': y*6.5},
            'locked': True
        },
        {
            'data': {'id': 'nine', 
                     'label': 'AutoGrid',
                     'parent': 'Features'},
            'position': {'x': x*1.25, 'y': y*6.5},
            'locked': True
        },
        {
            'data': {'id': 'ten', 
                     'label': 'X: Predictive Var.',
                     'parent': 'CNN'},
            'position': {'x': x*1, 'y': y*8.25},
            'locked': True
        },
        {
            'data': {'id': 'elev', 
                     'label': 'y: Response Var.',
                     'parent': 'CNN'},
            'position': {'x': x*2, 'y': y*8.25},
            'locked': True
        },
        {
            'data': {'id': 'twelve', 
                     'label': 'CNN: f(X) ~ y',
                     'parent': 'CNN'},
            'position': {'x': x*1.5, 'y': y*9.5},
            'locked': True
        },


        # Targets
        {'data': {'source': 'one', 'target': 'two'}},
        {'data': {'source': 'two', 'target': 'five'}},
        {'data': {'source': 'two', 'target': 'three'}},
        {'data': {'source': 'three', 'target': 'four'}},
        {'data': {'source': 'four', 'target': 'five'}},
        {'data': {'source': 'five', 'target': 'seven'}}, 
        {'data': {'source': 'six', 'target': 'seven'}}, 
]