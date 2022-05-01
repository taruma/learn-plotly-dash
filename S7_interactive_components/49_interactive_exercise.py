#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:


from dash import Dash, dcc, html, Input, Output

# import plotly.graph_objects as go


# Launch the application:

app = Dash(__name__)


# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:

app.layout = html.Div(
    [
        dcc.RangeSlider(
            min=-10,
            max=10,
            step=1,
            value=[-5, 5],
            id="range-slider",
            marks={i: {"label": str(i)} for i in range(-10, 11, 2)},
        ),
        html.H1(
            id="output-range-slider",
            # style={"fontSize": 40}
        ),
    ]
)

# Create a Dash callback:


@app.callback(Output("output-range-slider", "children"), Input("range-slider", "value"))
def callback_calc(slider_value):
    x1, x2 = slider_value
    return f"{x1} x {x2} = {x1 * x2}"


# Add the server clause:
if __name__ == "__main__":
    app.run_server(debug=True)
