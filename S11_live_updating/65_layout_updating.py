from dash import Dash, html, dcc, Input, Output

app = Dash()

crash_free = 0

app.layout = html.Div(
    [
        html.H1(id="live-update-text"),
        dcc.Interval(id="interval-component", interval=2000, n_intervals=0),
    ]
)


@app.callback(
    Output("live-update-text", "children"), Input("interval-component", "n_intervals")
)
def update_layout(n):
    return f"Crash free for {n} refreshes"


if __name__ == "__main__":
    app.run_server(debug=True)
