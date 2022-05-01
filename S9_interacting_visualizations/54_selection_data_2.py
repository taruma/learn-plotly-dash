from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import numpy as np
import pandas as pd

app = Dash()

np.random.seed(10)
x1 = np.linspace(0.1, 5, 50)
x2 = np.linspace(5.1, 10, 50)
y = np.random.randint(0, 50, 50)

df1 = pd.DataFrame({"x": x1, "y": y})
df2 = pd.DataFrame({"x": x1, "y": y})
df3 = pd.DataFrame({"x": x2, "y": y})

df = pd.concat([df1, df2, df3])

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(
                    id="plot",
                    figure={
                        "data": [go.Scatter(x=df.x, y=df.y, mode="markers")],
                        "layout": go.Layout(title="Scatterplot", hovermode="closest"),
                    },
                    style={"width": "70%", "display": "inline-block"},
                )
            ]
        ),
        html.Div(
            [html.H1(id="density", style={"paddingTop": 25})],
            # [html.Pre(id="density", style={"paddingTop": 25})],
            style={"width": "30%", "display": "inline-block", "verticalAlign": "top"},
        ),
    ]
)

import json


@app.callback(
    Output("density", "children"),
    Input("plot", "selectedData"),
    prevent_initial_call=True,
)
def find_density(selectedData):
    pts = len(selectedData["points"])
    rng_or_lp = list(selectedData.keys())
    rng_or_lp.remove("points")
    max_x = max(selectedData[rng_or_lp[0]]["x"])
    min_x = min(selectedData[rng_or_lp[0]]["x"])
    max_y = max(selectedData[rng_or_lp[0]]["y"])
    min_y = min(selectedData[rng_or_lp[0]]["y"])
    area = (max_x - min_x) * (max_y - min_y)
    d = pts / area
    # return json.dumps(selectedData, indent=2)
    # return f"{rng_or_lp[0]}"
    return f"density = {d:.2f}"
    # return f"{df.index.to_numpy()}"


if __name__ == "__main__":
    app.run_server(debug=True)
