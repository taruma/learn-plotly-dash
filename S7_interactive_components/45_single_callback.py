from jupyter_dash import JupyterDash
from dash import Dash, dcc, html, Input, Output

app = Dash("example")

app.layout = html.Div(
    [
        dcc.Input(id="my-id", value="Initial Text", type="text"),
        html.Div(id="my-div", style={"border": "2px blue solid"}),
    ]
)


@app.callback(
    Output(component_id="my-div", component_property="children"),
    [Input(component_id="my-id", component_property="value")],
    prevent_initial_call=True,
)
def update_output_div(input_value):
    return f"You entered: {input_value}"


if __name__ == "__main__":
    app.run_server(debug=True)
