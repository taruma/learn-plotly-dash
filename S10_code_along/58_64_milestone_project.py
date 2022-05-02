from dash import Dash, dcc, html, Input, Output, State
import plotly.graph_objects as go
import pandas as pd
import pandas_datareader as pdr
from datetime import date
import yfinance as yf
import numpy as np


df_nasdaq = pd.read_csv(
    r"source\Plotly-Dashboards-with-Dash\Data\NASDAQcompanylist.csv"
)

_symbol = df_nasdaq.Symbol.to_list()
_name = [f"{symbol} - {name}" for name, symbol in zip(df_nasdaq.Name, _symbol)]


options = [{"label": name, "value": symbol} for name, symbol in zip(_name, _symbol)]


app = Dash()

app.layout = html.Div(
    [
        html.H1("Stock Ticker Dashboard"),
        html.Div(
            [
                html.Div(
                    [
                        html.H3("Select stock symbols", style={"paddingRight": "30px"}),
                        dcc.Dropdown(
                            id="my-picker-drop",
                            options=options,
                            value=np.random.choice(_symbol, 5, replace=False),
                            multi=True,
                            searchable=True,
                            placeholder="Select Stocks/Symbol",
                        ),
                    ],
                    style={
                        "display": "inline-block",
                        "verticalAlign": "top",
                        "width": "30%",
                    },
                ),
                html.Div(
                    [
                        html.H3("Select start and end dates"),
                        dcc.DatePickerRange(
                            id="my-picker-date",
                            start_date=date(2019, 1, 1),
                            end_date=date(2021, 12, 31),
                            display_format="YYYY-MM-DD",
                            start_date_placeholder_text="YYYY-MM-DD",
                        ),
                    ],
                    style={"display": "inline-block"},
                ),
                html.Div(
                    [
                        html.Button(id="my-button", children="Submit"),
                    ],
                    style={"display": "inline-block"},
                ),
            ]
        ),
        # html.Pre(id="temporary"),
        dcc.Graph(
            id="my-graph",
            figure={
                "data": [{"x": [], "y": []}],
                "layout": go.Layout(
                    template="none",
                    xaxis={
                        "showgrid": False,
                        "showticklabels": False,
                        "zeroline": False,
                    },
                    yaxis={
                        "showgrid": False,
                        "showticklabels": False,
                        "zeroline": False,
                    },
                ),
            },
        ),
    ]
)


@app.callback(
    Output("my-graph", "figure"),
    # Output("temporary", "children"),
    Input("my-button", "n_clicks"),
    State("my-picker-drop", "value"),
    State("my-picker-date", "start_date"),
    State("my-picker-date", "end_date"),
    prevent_initial_call=True,
)
def callback_reader(n_clicks, symbol, start_date, end_date):
    # yf.pdr_override()
    df_stock = pdr.get_data_yahoo(symbol, start_date, end_date)
    # data_stock = yf.download(symbol, start_date, end_date)

    df_close = df_stock.Close.dropna(how="all", axis=1)

    data = [
        go.Scatter(
            x=df_close[sym_id].index,
            y=df_close[sym_id],
            mode="lines",
            # name=f'{sym_id} - {df_nasdaq.set_index("Symbol").at[sym_id, "Name"]}',
            name=sym_id,
        )
        for sym_id in df_close.columns
    ]

    title = f'{", ".join(df_close.columns)} Closing Prices'

    layout = go.Layout(title=title, hovermode="x", template="none", showlegend=True)

    # return f"{n_clicks} {symbol} {type(start_date)} {type(end_date)}"
    # return f"{data_stock}" + "<br>" + f"{n_clicks} {symbol} {start_date} {end_date}"
    # return f"{df_close}"
    return go.Figure(data, layout)


if __name__ == "__main__":
    app.run_server(debug=True)
