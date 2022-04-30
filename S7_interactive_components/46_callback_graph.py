from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from umaplotly import uma_template

df = pd.read_csv(r"source\Plotly-Dashboards-with-Dash\Data\gapminderDataFiveYear.csv")
df

pio.templates.default = uma_template

app = Dash("callbackgraph")

year_options = []
for year in df.year.unique():
    year_options.append({"label": str(year), "value": year})

app.layout = html.Div(
    [
        dcc.Graph(id="graph"),
        dcc.Dropdown(id="year-picker", options=year_options, value=df.year.min()),
    ]
)


@app.callback(Output("graph", "figure"), [Input("year-picker", "value")])
def update_figure(selected_year):

    filtered_df = df.loc[df.year == selected_year]

    traces = []

    for continent_name in filtered_df.continent.unique():
        df_by_continent = filtered_df.loc[filtered_df.continent == continent_name]
        traces.append(
            go.Scatter(
                x=df_by_continent.gdpPercap,
                y=df_by_continent.lifeExp,
                mode="markers",
                opacity=0.7,
                marker={"size": 15},
                name=continent_name,
            )
        )

    layout = go.Layout(
        title="My Plot",
        xaxis={"title": "GDP Per Cap", "type": "log"},
        yaxis={"title": "Life Expectancy"},
        hovermode="closest",
    )

    return go.Figure(data=traces, layout=layout)


if __name__ == "__main__":
    app.run_server(debug=True)
