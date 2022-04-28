import plotly.io as pio

uma = pio.templates["none"]

uma.layout.hovermode = "x unified"

uma.layout.images = [
    dict(
        source="https://hidrokit.github.io/hidrokit/assets/images/presskit/hidrokit-800x200-transparent.png",
        xref="paper",
        yref="paper",
        x=1,
        y=1.05,
        sizex=0.2,
        sizey=0.2,
        xanchor="right",
        yanchor="bottom",
        name="logo",
    )
]

uma_template = uma
