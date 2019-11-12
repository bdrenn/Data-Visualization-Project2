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


# Plot
fig = go.Figure()

fig.add_trace(go.Scatter(x=scanpath_graph, y=task_success_graph,
                    mode='markers'))
fig.add_trace(go.Scatter(x=scanpath_tree, y=task_success_tree,
                    mode='markers' ))


fig.show()

