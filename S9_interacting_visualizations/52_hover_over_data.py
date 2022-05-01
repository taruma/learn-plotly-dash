from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import json
import base64

app = Dash(__name__)

df = pd.read_csv(r"source\Plotly-Dashboards-with-Dash\Data\wheels.csv")


def encode_image(image_file):
    with open(image_file, "rb") as f_image:
        encoded = base64.b64encode(f_image.read())

    return "data:image/png;base64,{}".format(encoded.decode())


app.layout = html.Div(
    [
        html.Div(
            dcc.Graph(
                id="wheels-plot",
                figure={
                    "data": [
                        go.Scatter(
                            x=df.color,
                            y=df.wheels,
                            dy=1,
                            mode="markers",
                            marker={"size": 15},
                        )
                    ],
                    "layout": go.Layout(title="Test", hovermode="closest"),
                },
            ),
            style={"width": "40%", "float": "left"},
        ),
        html.Div(
            [
                html.Img(
                    id="hover-image",
                    src="children",
                    height=300,
                )
            ],
            style={"paddingTop": 35}
            # html.Pre(id="hover-data"),
        ),
    ]
)

from pathlib import Path


@app.callback(
    Output("hover-image", "src"),
    # Output("hover-data", "children")
    Input("wheels-plot", "hoverData"),
)
def callback_image(hoverData):
    wheel = hoverData["points"][0]["y"]
    color = hoverData["points"][0]["x"]
    path_file = Path(r"source\Plotly-Dashboards-with-Dash\Data\Images")
    return encode_image(
        path_file
        / (df.at[((df.wheels == wheel) & (df.color == color)).idxmax(), "image"])
    )  # , json.dumps(hoverData, indent=2)


if __name__ == "__main__":
    app.run_server(debug=True)
