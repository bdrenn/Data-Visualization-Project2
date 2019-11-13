import plotly.graph_objects as go
import numpy as np
import os 
import Preprocess as Data
from pathlib import Path

# Root Directory
path = Path(os.getcwd()).parent

#Graph Expert directory 
output_data_dir = path / 'OutputData'
graph_expert_data_dir = output_data_dir / 'GraphExpertData.csv'

#Tree Expert directory 
output_data_dir = path / 'OutputData'
tree_expert_data_dir = output_data_dir / 'TreeExpertData.csv'

#Tree Expert Data Object 
tree_expert_data = Data.TreeExpertData(tree_expert_data_dir)

scanpath_tree = tree_expert_data.ScanPathLength() # X-axis
task_success_tree = tree_expert_data.TaskSuccess() # Y-axis

#Graph Expert Data Object 
graph_expert_data = Data.GraphExpertData(graph_expert_data_dir)

scanpath_graph = graph_expert_data.ScanPathLength() # X-axis
task_success_graph = graph_expert_data.TaskSuccess() # Y-axis


#Graph General directory 
output_data_dir = path / 'OutputData'
graph_general_data_dir = output_data_dir / 'GraphGeneralData.csv'

#Tree General directory 
output_data_dir = path / 'OutputData'
tree_general_data_dir = output_data_dir / 'TreeGeneralData.csv'

#Tree General Data Object 
tree_general_data = Data.TreeGeneralData(tree_general_data_dir)

scanpath_tree_general = tree_general_data.ScanPathLength() # X-axis
task_success_tree_general = tree_general_data.TaskSuccess() # Y-axis

#Graph General Data Object 
graph_general_data = Data.GraphGeneralData(graph_general_data_dir)

scanpath_graph_general = graph_general_data.ScanPathLength() # X-axis
task_success_graph_general = graph_general_data.TaskSuccess() # Y-axis

# Plot
fig = go.Figure()

# Update plot sizing
fig.update_layout(
    width=1000,
    height=500,
    autosize=False,
    margin=dict(t=0, b=0, l=0, r=0),
    template="plotly_white",
)

fig.add_trace(go.Scatter(x=scanpath_graph, y=task_success_graph,
                    mode='markers'))
fig.add_trace(go.Scatter(x=scanpath_tree, y=task_success_tree,
                    mode='markers' ))

fig.update_scenes(
    aspectratio=dict(x=1, y=1, z=0.7),
    aspectmode="manual"
)
fig.add_trace(go.Scatter(x=scanpath_graph_general, y=task_success_graph_general,
                    mode='markers'))
fig.add_trace(go.Scatter(x=scanpath_tree_general, y=task_success_tree_general,
                    mode='markers' ))


fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            type = "buttons",
            direction = "left",
            buttons=list([
                dict(
                    args=["type", "scatter"],
                    label="General",
                    method="restyle"
                ),
                dict(
                    args=["type", "scatter"],
                    label="Expert",
                    method="restyle"
                )
            ]),
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.11,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)

# Add annotation
fig.update_layout(
    annotations=[
        go.layout.Annotation(text="Trace type:", showarrow=False,
                             x=0, y=1.08, yref="paper", align="left")
    ]
)
fig.show()




