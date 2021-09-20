import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc


# Titles
row_titles = dbc.Row(
    className='row-title-content',
    children= [
        # Title
       html.H2([
           "Molecular Dynamics Structures",
           ]
           ),
       # Subtitle
       html.H3([
           'Generation of MD-derived structures'
           ]
       )
    ]
)

# List of MD protocols
list_of_conf_ensembles = dbc.Row(
    className='ident-2',
    children = [
        
        html.P([
            html.I(className='ico fas fa-circle s1'),
            html.Mark(
                'apoMD',
                className='pill pill-red'
            ),
            ': MD of the ', 
            html.B('protein apo state'), ':',
            html.Br(),
            html.Em('- Ligands and other protein entities were removed.')
        ]),
        html.P([
            html.I(className='ico fas fa-circle s1'),
            html.Mark(
                'ligMD',
                className='pill pill-orange'
            ),
            ': MD of the protein holo state (', 
            html.B('ligand-bound'), ').',
            html.Br(),
            html.Em('- Bound ligand at the active site was kept.')
        ]),
        html.P([
            html.I(className='ico fas fa-circle s1'),
            html.Mark(
                'etaMD',
                className='pill pill-blue'
            ),
            ': MD of the protein apo state ',
            html.B('solvated'),
            ' with 20% of ',
            html.B('ethanol.'),
            html.Br(),
            '- ',
            html.A('pyMDMix',
            href = 'http://mdmix.sourceforge.net/', target = '_blank'),
            html.Em(' package was used to solvate the protein.')
        ]),
    ]

)


# Text column
text_content_col_1 = dbc.Col(
    className='row-text-content',
    lg = 6, md = 12,
    children=[
        html.H4([
           'Molecular Dynamics'
           ]
        ),
        html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            'We performed ',
            'Molecular dynamics (MD) simulations',
            ' to explore the ',
            html.B('conformational space'),
            ' of the CDK2 protein.'
           ]
       ),
        html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            'MD simulations were performed using ',
            html.A('Amber 2018.',
            href = 'http://ambermd.org/', target = '_blank')
           ]
       ),
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            'Each of the ',
            'four representative',
            ' PDB conformations was combined with ',
            html.B(
                'three MD protocols:'
                )
           ]
       ),
       list_of_conf_ensembles, 
        html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            "As a result ",
            html.B("12 different systems"),
            " were simulated, each one consisting of:"
           ],
        ),
       html.Ul(
           [
            html.Li("Five replicas of 20 ns each."),
            html.Li("1,000 frames (conformations) per replica."),
            html.Li("5,000 frames (conformations) per system."),
           ], 
           className='ident-3'
       ),
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            'A total of ',
            html.Mark(html.B('60,000 protein conformations')),
            ' were generated.'
           ],
       ),
       
    ]
)

text_content_col_2 = dbc.Col(
    className='row-text-content',
    lg = 6, md = 12,
    children=[ 
       html.H4([
           'K-means clustering'
           ]
       ),
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            "Structural analysis of the ",
            html.B("MD trajectories"),
            " was performed using the ",
            html.A("pytraj library",
            href='https://amber-md.github.io/pytraj/latest/index.html', target='_blank'),
            "."
           ],
       ),
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            html.B("k-means clustering"),
            " was performed to select representative structures from MD trajectories:"
           ],
       ),
       html.Ul(
           [
            html.Li(["Performed using ",
                html.A("scikit-learn", 
                        href='https://scikit-learn.org/', 
                        target='_blank'),
                "."]
                ),
            html.Li([html.Em("k = 30"),
                    " to generate ", html.B("30 clusters"), " per system"]),
            html.Li(["The ", 
            html.B("medoid structure"),
            " of each cluster was selected."]),
           ], 
           className='ident-3'
       ),
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            "A total of ",
            html.B(html.Mark("360 MD representative structures")),
            " were extracted."
           ], 
       ),
       html.H4([
           'Energy Minimization'
           ]
        ),
       html.P(
           [
            html.I(className='ico fas fa-chevron-right'),
            html.B("Potential energy minimization"),
            " was applied to the:",
            html.Ul(
                [
                    html.Li([
                        '402 CRYS structures'
                    ]),
                    html.Li([
                        '360 MD structures'
                    ]),
                ], 
                className='ident-2'
            ),
           ],
       ),
    #    html.P(
    #        [
    #         html.I(className='ico fas fa-chevron-right'),
    #         'Finally ',
    #         html.B("1,524 conformations"),
    #         " was applied to the:",
    #        ],
    #    ),
    ]
)


# All Content
row_content = dbc.Row(
    children=[
        # Column 1
        text_content_col_1,
        # Column 2
        text_content_col_2 
    ]
)


col_contents = [
   row_titles,
   row_content 
]