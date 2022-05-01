from dash import Dash, dcc, html, Input, Output, State

app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Input(id="number-in", value=1, style={"fontSize": 24}),
        html.Button(
            id="submit-button",
            n_clicks=0,
            children="Submit Here",
            style={"fontSize": 24},
        ),
        html.H1(id="number-out"),
    ]
)


@app.callback(
    Output("number-out", "children"),
    Input("submit-button", "n_clicks"),
    State("number-in", "value"),
)
def output(n_clicks, number):
    return f'{number} was typed in, and button was clicked {n_clicks} times'


if __name__ == "__main__":
    app.run_server(debug=True)
