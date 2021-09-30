import plotly
import plotly.graph_objects as go

colors = ['Empty', 
          'Hydrophilic', 
          'Hydrophobic', 
          'H-bond Donor', 
          'H-bond Acceptor', 
          'Aromatic'
          ]

palette_channels = ['#C2BBAA', 
           '#666AE9', 
           '#66BFE9',
           '#E94E4E', 
           '#60DA59', 
           'orange']

prot_colors = {
                '1fin': '#B44D4D',
                '4fku': '#27879C',
                '3pxf': '#A6832E',
                '5a14': '#2F917C'
            }
conf_colors = list(prot_colors.values()) + list(prot_colors.values())

def plot_povme_pockets(X, 
                       prot_xyz,
                       label_confs,
                       label_channels, 
                       palette_channels = palette_channels, 
                       palette_confs = conf_colors,
                       focus_pocket = True,
                       opacity = 0.5):
    
    
    fig = go.Figure()
    n_pkts, s_x, s_y, s_z, n_channels = X.shape

    assert len(label_confs) == n_pkts
    assert len(label_channels) == n_channels
    assert prot_xyz.shape[0] == n_pkts
    
    if focus_pocket:
        scene = dict(
          xaxis = dict(nticks=12, range=[0,s_x],
                       backgroundcolor="#E7E2D7",
                       gridcolor="#B2A078"),
          yaxis = dict(nticks=12, range=[0,s_y],
                      backgroundcolor="#E7E2D7",
                       gridcolor="#B2A078"),
          zaxis = dict(nticks=12, range=[0,s_z],
                      backgroundcolor="#E7E2D7",
                       gridcolor="#B2A078"),
          aspectratio=dict(x=1, y=1, z=1)
        )
        prot_dot_line_width = 3
        prot_dot_size = 9
    else:
        scene = dict(
          xaxis = dict(
                       backgroundcolor="rgba(0,0,0,0)",
                       gridcolor="#B2A078"),
          yaxis = dict(
                      backgroundcolor="rgba(0,0,0,0)",
                       gridcolor="#B2A078"),
          zaxis = dict(
                      backgroundcolor="rgba(0,0,0,0)",
                       gridcolor="#B2A078"),
          aspectratio=dict(x=1, y=1, z=1)
        )
        prot_dot_line_width = 0
        prot_dot_size = 4

    for i_pkt, conf_label in zip(range(n_pkts), label_confs):
        for chn, color, c_label in zip(range(n_channels), 
                                     palette_channels, 
                                     label_channels):
            pkt_chn = X[i_pkt, :, :, :, chn]
            x, y, z = pkt_chn.nonzero()
            fig.add_trace(
                go.Scatter3d(
                  x = x, y = y, z = z,
                  mode  = 'markers',
                  visible = False,
                  name = c_label,
                    hoverinfo='skip',
                  marker = dict(
                      size    = 5,
                      opacity = opacity,
                      color   = color
                    )
                  )
            )
        # add protein as a extra channel
        prot_coords = prot_xyz[i_pkt]
        x, y, z = prot_coords.squeeze().T
        fig.add_trace(
                go.Scatter3d(
                  x = x, y = y, z = z,
#                   mode  = 'lines',
                  visible = False,
                  name = conf_label + ' backbone',
                    hoverinfo='skip',
                  marker = dict(
                      size    = prot_dot_size,
                      opacity = opacity,
                      color   = palette_confs[i_pkt],
                      line_width = prot_dot_line_width,
                      line_color = 'black'
                    ),
                  line=dict(
                    color=palette_confs[i_pkt],
                    width=10,
                ),
                
              ) 
         )
    # Update the number of channels
    n_channels += 1
    for i in range(n_channels):
        fig.data[i].visible = True

    steps = []
    for i in range(n_pkts):
        step = dict(
          method="update",
          args=[{"visible": [False] * len(fig.data)},
                {"title": "Conformation: " + label_confs[i]}], 
          )
        
        step["args"][0]["visible"][i*n_channels:(i+1)*n_channels] = [True] * n_channels
        steps.append(step)


    sliders = [dict(
      active=0,
      currentvalue={"prefix": "Conformation: "},
      pad={"t": 0},
      steps=steps
    )]

    fig.update_layout(
      sliders=sliders,
      height = 550,
      scene = scene,
        paper_bgcolor = '#E1D8C3',
        plot_bgcolor = '#EDEBE1',
        template='plotly_white',
        hoverlabel=dict(
            bgcolor = 'white',
            font_size=14
        ),
        legend=dict(
            font=dict(
                color='#333333',
                size=11),
            orientation="v",
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bordercolor = '#333333',
            borderwidth = 1,
            bgcolor="#E7E3D6"
        ),
        margin=dict(l=10, 
                    r=10, 
                    t=35, 
                    b=5),
        modebar=dict(orientation='v', 
                     activecolor='#1f76b1')
    )

    return fig