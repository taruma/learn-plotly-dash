from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import base64
from pathlib import Path

df = pd.read_csv(r"source\Plotly-Dashboards-with-Dash\Data\wheels.csv")


def encode_image(image_file):
    with open(image_file, "rb") as f_image:
        encoded = base64.b64encode(f_image.read())

    return "data:image/png;base64,{}".format(encoded.decode())


app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.RadioItems(
            id="wheels",
            options=[{"label": i, "value": i} for i in df.wheels.unique()],
            value=1,
        ),
        html.Div(id="wheels-output"),
        html.Hr(),
        dcc.RadioItems(
            id="colors",
            options=[{"label": i, "value": i} for i in df.color.unique()],
            value="blue",
        ),
        html.Div(id="colors-output"),
        html.Hr(),
        # html.Div(id="test", children="test"),
        html.Img(id="display-image", src="children", height=300),
    ],
    style={"fontFamily": "helvetica", "fontSize": 18},
)


@app.callback(Output("wheels-output", "children"), [Input("wheels", "value")])
def callback_a(wheels_value):
    return f"You choose {wheels_value}"


@app.callback(Output("colors-output", "children"), [Input("colors", "value")])
def callback_b(colors_value):
    return f"You choose {colors_value}"


@app.callback(
    Output("display-image", "src"), Input("wheels", "value"), Input("colors", "value")
)
def callback_image(wheel, color):
    image_dir = Path(r"source\Plotly-Dashboards-with-Dash\Data\Images")
    image_name = df.at[((df.wheels == wheel) & (df.color == color)).idxmax(), "image"]
    image_file = image_dir / image_name
    return encode_image(image_file)


if __name__ == "__main__":
    app.run_server(debug=True)
