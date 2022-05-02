from typing import Counter
from dash import Dash, html, dcc, Input, Output
import requests
import plotly.graph_objects as go

app = Dash()

app.layout = html.Div(
    [
        html.Div(
            [html.Iframe(src="https://hidrokit.github.io", height=500, width=1200)]
        ),
        html.Div(
            [
                html.Pre(id="counter-text", children="Active Flights Worldwide"),
                dcc.Graph(id="live-update-graph", style={"width": 1200}),
                dcc.Interval(id="interval-component", interval=6000, n_intervals=0),
            ]
        ),
    ]
)

counter_list = []


@app.callback(
    Output("counter-text", "children"), Input("interval-component", "n_intervals")
)
def update_layout(n):
    url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1\
           &mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    data = res.json()
    counter = 0
    for element in data["stats"]["total"]:
        counter += data["stats"]["total"][element]
    counter_list.append(counter)
    return f"Active flights Worldwide {counter}"


@app.callback(
    Output("live-update-graph", "figure"), Input("interval-component", "n_intervals")
)
def update_graph(n):
    fig = go.Figure(
        data=[
            go.Scatter(
                x=list(range(len(counter_list))),
                y=counter_list,
                mode="lines+markers",
            )
        ]
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
