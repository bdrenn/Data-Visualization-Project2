import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv("Graph_G_Finalc.csv")
df1 = pd.read_csv("Tree_G_Finalc.csv")

GGraph_minute = df['minute']
GGraph_fixTime = df['average_fixation']
GGraph_width = df['total_people']

GTree_minute = df1['minute']
GTree_fixTime = df1['average_fixation']
GTree_width = df1['total_people']



fig = go.Figure(
    data=[go.Bar(x=GGraph_minute,y=GGraph_fixTime,width= GGraph_width/10, showlegend=False),
        go.Bar(x=GTree_minute, y=GTree_fixTime, width=GTree_width/10, showlegend=False)],

    layout=go.Layout(barmode='overlay'),

)

fig.add_trace(go.Bar(x=GGraph_minute, y=GGraph_fixTime,width= GGraph_width/10,
                     name="General Graph",
                     text=GGraph_width,
                     hovertemplate="Minute: %{x} <br>Seconds: %{y}</br>Participants: %{text}"
                     ))

fig.add_trace(go.Bar(x=GTree_minute, y=GTree_fixTime, width=GTree_width/10,
                     name="General Tree",
                     text=GTree_width,
                     hovertemplate="Minute: %{x} <br>Seconds: %{y}</br>Participants: %{text}"
                     ))

fig.update_layout(
    legend=go.layout.Legend(
        x=0,
        y=1
    ),
    title_text='General Graph and Tree Fixation Times',
    xaxis_title="Minutes",
    yaxis_title="Fixation Time (seconds)"

)

# fig.show()
fig.write_html('first_figure.html', auto_open=True)
