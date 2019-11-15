import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv("Graph_E_Finalc.csv")
df1 = pd.read_csv("Tree_E_Finalc.csv")

EGraph_minute = df['minute']
EGraph_fixTime = df['average_fixation']
EGraph_width = df['total_people']

ETree_minute = df1['minute']
ETree_fixTime = df1['average_fixation']
ETree_width = df1['total_people']



fig = go.Figure(
    data=[go.Bar(x=EGraph_minute,y=EGraph_fixTime,width= EGraph_width/(EGraph_width.max() + 1), name="Expert Graph",
                 text=EGraph_width, hovertemplate="Minute: %{x} <br>Seconds: %{y}</br>Participants: %{text}",
                 showlegend=True),
        go.Bar(x=ETree_minute, y=ETree_fixTime, width=ETree_width/(EGraph_width.max() + 1), opacity=.7,
               name="Expert Tree", text=EGraph_width,
               hovertemplate="Minute: %{x} <br>Seconds: %{y}</br>Participants: %{text}", showlegend=True)],

    layout=go.Layout(barmode='overlay'),

)

fig.update_layout(
    legend=go.layout.Legend(
        x=0,
        y=1
    ),
    title_text='Graph and Tree Fixation Times',
    xaxis_title="Minutes",
    yaxis_title="Fixation Time (seconds)",
    yaxis_dtick=15,
    xaxis_dtick=1,
    bargap=1,
    yaxis_range=[0, 60]
)

# fig.show()
fig.write_html('first_figure.html', auto_open=True)
