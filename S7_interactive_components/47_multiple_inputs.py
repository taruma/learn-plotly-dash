from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv(r"source\Plotly-Dashboards-with-Dash\Data\mpg.csv")

app = Dash(__name__)

features = df.columns


app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Dropdown(
                    id="xaxis",
                    options=[{"label": i, "value": i} for i in features],
                    value="displacement",
                )
            ],
            style={"width": "48%", "display": "inline-block"},
        ),
        html.Div(
            [
                dcc.Dropdown(
                    id="yaxis",
                    options=[{"label": i, "value": i} for i in features],
                    value="mpg",
                )
            ],
            style={"width": "48%", "display": "inline-block"},
        ),
        dcc.Graph(id="feature-graphic"),
    ],
    style={"padding": 10},
)


@app.callback(
    Output("feature-graphic", "figure"),
    [Input("xaxis", "value"), Input("yaxis", "value")],
)
def update_graph(xaxis_name, yaxis_name):
    return {
        "data": [
            go.Scatter(
                x=df[xaxis_name],
                y=df[yaxis_name],
                text=df.name,
                mode="markers",
                marker={
                    "size": 10,
                    "opacity": 0.5,
                    "line": {"width": 0.5, "color": "black"},
                },
            )
        ],
        "layout": go.Layout(
            title="My Dashboard for MPG",
            xaxis={"title": xaxis_name},
            yaxis={"title": yaxis_name},
        ),
    }


if __name__ == "__main__":
    app.run_server(debug=True)
