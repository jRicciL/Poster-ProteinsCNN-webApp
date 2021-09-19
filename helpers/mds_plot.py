import plotly.graph_objects as go
import pandas as pd
import numpy as np


def get_mds_layout():
    '''
    Returns a plotly layout for the cMDS plots
    '''
    fig = go.Figure()
    # AXES
    fig.update_xaxes(ticks='outside', 
                     showline=True, 
                     linewidth=2., 
                     title_font=dict(size=22),
                     gridcolor='#E1D8C3',
                     linecolor='#273139', 
                     mirror = True)
    fig.update_yaxes(ticks='outside', 
                     showline=True, 
                     title_font=dict(size=22),
                     gridcolor='#E1D8C3',
                     linewidth=2., 
                     linecolor='#273139', 
                     mirror = True)
    fig.update_layout(
        height=400,
        paper_bgcolor = '#E1D8C3',
        plot_bgcolor = '#EDEBE1',
        template='plotly_white',
        hoverlabel=dict(
            bgcolor = 'white',
            font_size=14
        ),
        xaxis = dict(
            title={
                'text': 'First Dimension',
                'standoff': 0,
                'font': {
                    'size': 17
                } 
            },
            zeroline=True, 
            zerolinecolor='#BDB5A3', 
            zerolinewidth=2,
        ),
        yaxis = dict(
            title={
                'text': 'Second Dimension',
                'standoff': 0,
                'font': {
                    'size': 17
                }
            },
            zeroline=True, 
            zerolinecolor='#BDB5A3', 
            zerolinewidth=2
        ),
        legend=dict(
            font=dict(
                color='#333333',
                size=12.5),
            orientation="v",
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor="#E7E3D6"
        ),
        dragmode='pan',
        margin=dict(l=30, 
                    r=30, 
                    t=5, 
                    b=30),
        modebar=dict(orientation='v', 
                     activecolor='#1f76b1')
    )

    return fig


def add_CRYS_mds_trace(
        fig, 
        df, 
        x_col, 
        y_col, 
        hue_col = 'Conformation', 
        size_col = 'Pocket Volume (Pkt)', 
        palette = ['#2a7885', '#6EB9B6', '#f64a3b', 
                    '#fecc6a', '#76C376'], 
        preselected_confs = None,
        show_legend = True,
        single_size = 8,
        size_scale = 1.5,
        marker_symbol = 'circle',
        hoverinfo = 'text',
        line_width = 0,
        line_color = 'black',
        opacity = 0.7,
        ):
    
    labels = df[hue_col].unique()
    assert len(labels) == len(palette)
    
    df_ = df.copy()
    size_min = 1
    if size_col == '':
        df_[size_col] = single_size
        size_min = single_size
    size = df_[size_col] 

    for label, color in zip(labels, palette):
        subset = df_.query(f'{hue_col} == "{label}"')
        size = subset[size_col]

        formatted_text = [
            f'<b>Conf:</b> {idx}' + 
            f'<br><b>Ligand:</b> {lig}'+
            f'<br><b>Ligand MW:</b> {lig_mass} '  +
            f'<br><b>Pkt volume:</b> {pkt_vol} A<sup>3</sup>'  
            for idx, lig, lig_mass, pkt_vol in  
            zip(subset['PDB-id'], 
                subset.Ligand, 
                subset.LigMass,
                subset['Pocket Volume (Pkt)'])]
        fig.add_trace(
            go.Scatter(
                x = subset[x_col],
                y = subset[y_col],
                name=label,
                showlegend=show_legend,
                mode='markers',
                marker_symbol = marker_symbol,
                marker=dict(
                    color=color,
                    size=size,
                    sizemode='diameter',
                    sizeref= size_scale*max(size)/(5.**2),
                    sizemin=1,
                    line_width=line_width,
                    line_color = line_color
                ),           
                #selectedpoints = preselected_confs,
                selected=dict(
                    marker=dict(
                        opacity=1
                    )
                ),
                opacity=opacity,
                hoverinfo=hoverinfo,
                hovertext=formatted_text
            )
        )

    return fig


def add_REFS_mds_trace(
        fig, 
        df, x_col, y_col, 
        color = '#2CEA00',
        size_col = 'Pocket Volume (Pkt)',
        marker_symbol = 'circle',
        size_scale = 1.5,
        single_size = 8):
    subset = df.copy()
    size_min = 1
    if size_col == '':
        subset[size_col] = single_size
        size_min = single_size
    size = subset[size_col]
    
    formatted_text = [
            f'<b>Conf:</b> {idx}' + 
            f'<br><b>Ligand:</b> {lig}'+
            f'<br><b>Ligand MW:</b> {lig_mass} '  +
            f'<br><b>Pkt volume:</b> {pkt_vol} A<sup>3</sup>'  
            for idx, lig, lig_mass, pkt_vol in  
            zip(subset['PDB-id'], 
                subset.Ligand, 
                subset.LigMass,
                subset['Pocket Volume (Pkt)'])]
    
    fig.add_trace(
        go.Scatter(
            x = df[x_col],
            y = df[y_col],
            name = 'Refs',
            showlegend=False,
            mode = 'markers+text',
            text = df['PDB-id'], 
            textposition="top center",
            textfont = dict(
                color='black', 
                size=18,),
            marker_symbol = marker_symbol,
            marker=dict(
                color = 'rgba(0,0,0,0)',
                size = size,
                sizemode = 'diameter',
                sizeref = size_scale*max(size)/(5.**2),
                sizemin = size_min,
                line_width = 2,
                line_color = 'black'
            ),           
            #selectedpoints = preselected_confs,
            selected=dict(
                marker=dict(
                    opacity=1
                )
            ),
            opacity=1,
            hoverinfo='skip',
        )
    )

    return fig


def add_arrows_trace(fig, df, x_col_1, y_col_1, 
                     x_col_2, y_col_2):
    df_cols = df[[x_col_1, y_col_1, 
                     x_col_2, y_col_2]].values
    for x1, y1, x2, y2 in df_cols:
         fig.add_trace(
            go.Scatter(
                x = [x1, x2],
                y = [y1, y2],
                mode='lines',
                hoverinfo='skip',
                showlegend=False,
                line_color = 'cyan')
         )
    return fig