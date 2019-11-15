import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("Graph_E_Finalc.csv")
df1 = pd.read_csv("Tree_E_Finalc.csv")

EGraph_minute = df['minute']
EGraph_fixTime = df['average_fixation']
EGraph_width = df['total_people']

ETree_minute = df1['minute']
ETree_fixTime = df1['average_fixation']
ETree_width = df1['total_people']

fig = go.Figure(
    data=[go.Bar(x=EGraph_minute,y=EGraph_fixTime,width= EGraph_width/10,name='Graph'),
        go.Bar(x=ETree_minute, y=ETree_fixTime, width=ETree_width/10, opacity=0.7,name='Tree')],

    layout=go.Layout(
        title= {
        'text': "Width: Amount of People Per Fixation Time by Minute",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        barmode='overlay',
        bargap = 1.0,
        xaxis_title = "Minutes",
        yaxis_title = "Average Fixation Time",)
)
#fig.update_traces(opacity=0.6)#this makes both transparent...

# fig.show()
fig.write_html('first_figure.html', auto_open=True)
