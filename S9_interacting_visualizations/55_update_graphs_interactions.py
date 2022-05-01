from importlib.util import LazyLoader
from dash import Dash, dcc, html, Input, Output
from matplotlib.pyplot import margins
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from numpy import random

app = Dash(__name__)

df = pd.read_csv(r"source\Plotly-Dashboards-with-Dash\Data\mpg.csv")

# add jitter
df["year"] = random.randint(-4, 5, len(df)) * 0.1 + df.model_year


app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(
                    id="mpg-scatter",
                    figure={
                        "data": [
                            go.Scatter(
                                x=df.year + 1900,
                                y=df.mpg,
                                text=df.name,
                                hoverinfo="text+y+x",
                                mode="markers",
                            )
                        ],
                        "layout": go.Layout(
                            title="MPG Data",
                            xaxis={"title": "Model Year"},
                            yaxis={"title": "MPG"},
                            hovermode="closest",
                        ),
                    },
                )
            ],
            style={"width": "50%", "display": "inline-block"},
        ),
        html.Div(
            [
                dcc.Graph(
                    id="mpg-line",
                    figure={
                        "data": [go.Scatter(x=[0, 1], y=[0, 1], mode="lines")],
                        "layout": go.Layout(title="Acceleration", margin={"l": 0}),
                    },
                )
            ],
            style={"width": "20%", "height": "50%", "display": "inline-block"},
        ),
        html.Div(
            [dcc.Markdown(id="mpg-stats")],
            style={"width": "20%", "height": "50%", "display": "inline-block"},
        )
        # html.Pre(id="pre-text", style={"paddingTop": 35, "width": "30%"}),
    ]
)

import json


@app.callback(
    [Output("mpg-line", "figure"), Output("mpg-stats", "children")],
    Input("mpg-scatter", "hoverData"),
    prevent_initial_call=True,
)
def callback_graph(hoverData):
    v_index = hoverData["points"][0]["pointIndex"]
    figure = {
        "data": [
            go.Scatter(
                x=[0, 1],
                y=[0, 60 / df.iloc[v_index].loc["acceleration"]],
                mode="lines",
                line={"width": 2 * df.iloc[v_index].cylinders},
            )
        ],
        "layout": go.Layout(
            title=df.iloc[v_index].loc["name"],
            margin={"l": 0},
            height=300,
            xaxis={"visible": False},
            yaxis={"visible": True, "range": [0, 60 / df.acceleration.min()]},
        ),
    }
    stats = f"""
    __{df.iloc[v_index].cylinders}__ cylinders

    {df.iloc[v_index].displacement}cc displacement
    
    0 to 60mph in `{df.iloc[v_index].acceleration}` seconds
    """
    return figure, stats


if __name__ == "__main__":
    app.run_server(debug=True)
