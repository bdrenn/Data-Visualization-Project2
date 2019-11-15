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

df = pd.read_csv("Graph_E_Finalc.csv")
df1 = pd.read_csv("Tree_E_Finalc.csv")

EGraph_minute = df['minute']
EGraph_fixTime = df['average_fixation']
EGraph_width = df['total_people']

ETree_minute = df1['minute']
ETree_fixTime = df1['average_fixation']
ETree_width = df1['total_people']


fig = go.Figure(
    data=[go.Bar(x=GGraph_minute,y=GGraph_fixTime,width= GGraph_width/(GGraph_width.max() + 1),
                 name="General Graph", text=GGraph_width,
                 hovertemplate="Minute: %{x} <br>Seconds: %{y}</br>Participants: %{text}", showlegend=True,)],
                 #marker_color='blue',)],

    layout=go.Layout(barmode='overlay'),

)

fig.add_trace(go.Bar(x=GTree_minute, y=GTree_fixTime, width=GTree_width/(GGraph_width.max() + 1), opacity=.7,
               name="General Tree",
               text=GGraph_width, hovertemplate="Minute: %{x} <br>Seconds: %{y}</br>Participants: %{text}",
               showlegend=True,
               #marker_color='red',
                     visible=True,),
              )


fig.add_trace(go.Bar(x=EGraph_minute,y=EGraph_fixTime,width= EGraph_width/(EGraph_width.max() + 1), name="Expert Graph",
                     text=EGraph_width, hovertemplate="Minute: %{x} <br>Seconds: %{y}</br>Participants: %{text}",
                     showlegend=True,
                     #marker_color='blue',
                     visible=False),
              )

fig.add_trace(go.Bar(x=ETree_minute, y=ETree_fixTime, width=ETree_width/(EGraph_width.max() + 1), opacity=.7,
                     name="Expert Tree", text=EGraph_width,
                     hovertemplate="Minute: %{x} <br>Seconds: %{y}</br>Participants: %{text}",
                     showlegend=True,
                     #marker_color='red',
                     visible=False),)

fig.update_layout(
    legend=go.layout.Legend(
        x=0,
        y=1
    ),
    title_text='Graph and Tree Fixation Time Per Minute',
    xaxis_title="Minutes",
    yaxis_title="Fixation Time (seconds)",
    yaxis_dtick=15,
    xaxis_dtick=1,
    bargap=1,
    yaxis_range=[0, 60]
)

fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            type="buttons",
            direction="right",
            active=0,
            x=0.57,
            y=1.2,
            buttons=list([
                dict(label="General",
                     method="update",
                     args=[{"visible": [True, True, False, False]}]),
                dict(label="Expert",
                     method="update",
                     args=[{"visible": [False, False, True, True]}]),
            ]),
        )
    ])

# fig.show()
fig.write_html('Bar_Graph.html', auto_open=True)
