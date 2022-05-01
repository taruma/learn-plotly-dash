from dash import Dash, dcc, html, Input, Output

#######
# This makes a 3x3 scatterplot of wheels.csv, and sends
# the results of a selection to the screen as a JSON object.
######
import plotly.graph_objs as go
import pandas as pd
import json

app = Dash()

df = pd.read_csv(r"source\Plotly-Dashboards-with-Dash\Data\wheels.csv")

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(
                    id="wheels-plot",
                    figure={
                        "data": [
                            go.Scatter(
                                x=df["color"],
                                y=df["wheels"],
                                dy=1,
                                mode="markers",
                                marker={
                                    "size": 12,
                                    "color": "rgb(51,204,153)",
                                    "line": {"width": 2},
                                },
                            )
                        ],
                        "layout": go.Layout(
                            title="Wheels & Colors Scatterplot",
                            xaxis={"title": "Color"},
                            yaxis={"title": "# of Wheels", "nticks": 3},
                            hovermode="closest",
                        ),
                    },
                )
            ],
            style={"width": "70%", "display": "inline-block"},
        ),
        html.Div(
            [html.Pre(id="selection", style={"paddingTop": 25})],
            style={"width": "30%", "display": "inline-block", "verticalAlign": "top"},
        ),
    ]
)


@app.callback(Output("selection", "children"), [Input("wheels-plot", "selectedData")])
def callback_image(selectedData):
    return json.dumps(selectedData, indent=2)


if __name__ == "__main__":
    app.run_server(debug=True)
