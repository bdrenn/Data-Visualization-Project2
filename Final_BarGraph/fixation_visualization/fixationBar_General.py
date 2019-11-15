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
    data=[go.Bar(x=GGraph_minute,y=GGraph_fixTime,width= GGraph_width/(GGraph_width.max() + 1),
                 name="General Graph", text=GGraph_width,
                 hovertemplate="Minute: %{x} <br>Seconds: %{y}</br>Participants: %{text}", showlegend=True),
        go.Bar(x=GTree_minute, y=GTree_fixTime, width=GTree_width/(GGraph_width.max() + 1), opacity=.7,
               name="General Tree",
               text=GGraph_width, hovertemplate="Minute: %{x} <br>Seconds: %{y}</br>Participants: %{text}",
               showlegend=True)],

    layout=go.Layout(barmode='overlay'),

)


fig.update_layout(
    legend=go.layout.Legend(
        x=0,
        y=1
    ),
    title_text='General Graph and Tree Fixation Times',
    xaxis_title="Minutes",
    yaxis_title="Fixation Time (seconds)",
    yaxis_dtick=15,
    xaxis_dtick=1,
    bargap=1,
    yaxis_range=[0, 60]
)

# fig.show()
fig.write_html('first_figure.html', auto_open=True)
