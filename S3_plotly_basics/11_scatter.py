import numpy as np
import plotly.graph_objects as go

np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [
    go.Scatter(
        x=random_x,
        y=random_y,
        mode="markers",
        marker=dict(
            size=12, color="rgb(51, 204, 153)", symbol="pentagon", line=dict(width=2)
        ),
    )
]
layout = go.Layout(
    title="Hello First Plot",
    xaxis={"title": "MY X AXIS"},
    yaxis=dict(title="MY Y AXIS"),
    hovermode="closest",
)

fig = go.Figure(data=data, layout=layout)

# fig.write_html("scatter.html")
fig.show()
