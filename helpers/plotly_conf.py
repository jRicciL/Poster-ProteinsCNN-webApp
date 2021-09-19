import plotly.graph_objects as go

mode_bar_buttons = ["toImage", "autoScale2d",
                    "toggleSpikelines", "hoverCompareCartesian", 
                    "hoverClosestCartesian"]
plotly_conf = dict(
    displaylogo=False,
    displayModeBar=True,
    scrollZoom= True,
    modeBarButtonsToRemove=mode_bar_buttons
)