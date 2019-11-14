import plotly.graph_objects as go
import plotly
import numpy as np
import os 
import Preprocess 
from pathlib import Path
import plotly.offline as offline

# Root Directory
path = Path(os.getcwd()).parent

#Graph Expert directory 
output_data_dir = path / 'OutputData'
graph_expert_data_dir = output_data_dir / 'GraphExpertData.csv'

#Graph General directory 
output_data_dir = path / 'OutputData'
graph_general_data_dir = output_data_dir / 'GraphGeneralData.csv'

#Tree Expert directory 
output_data_dir = path / 'OutputData'
tree_expert_data_dir = output_data_dir / 'TreeExpertData.csv'

#Tree General directory 
output_data_dir = path / 'OutputData'
tree_general_data_dir = output_data_dir / 'TreeGeneralData.csv'



#Tree Expert Data Object 
tree_expert_data = Preprocess.TreeExpertData(tree_expert_data_dir)
scanpath_tree_expert = tree_expert_data.ScanPathLength() # X-axis
task_success_tree_expert = tree_expert_data.TaskSuccess() # Y-axis
average_saccade_tree_expert = tree_expert_data.AverageSaccadeLength() # Hover
average_success_tree_expert = tree_expert_data.AverageTaskSuccess() # Line success
average_scanpath_tree_expert = tree_expert_data.AverageScanpathLength() # Line scanpath


#Tree General Data Object
tree_general_data = Preprocess.TreeGeneralData(tree_general_data_dir)
scanpath_tree_general = tree_general_data.ScanPathLength() # X-axis
task_success_tree_general = tree_general_data.TaskSuccess() # Y-axis
average_saccade_tree_general = tree_general_data.AverageSaccadeLength() # Hover
average_success_tree_general = tree_general_data.AverageTaskSuccess() # Line success
average_scanpath_tree_general = tree_general_data.AverageScanpathLength() # Line Scanpath

#Graph Expert Data Object 
graph_expert_data = Preprocess.GraphExpertData(graph_expert_data_dir)
scanpath_graph_expert = graph_expert_data.ScanPathLength() # X-axis
task_success_graph_expert = graph_expert_data.TaskSuccess() # Y-axis
average_saccade_graph_expert = graph_expert_data.AverageSaccadeLength() # Hover
average_success_graph_expert = graph_expert_data.AverageTaskSuccess() # Line success
average_scanpath_graph_expert = graph_expert_data.AverageScanpathLength() # Line Scanpath

#Graph General Data Object
graph_general_data = Preprocess.GraphGeneralData(graph_general_data_dir)
scanpath_graph_general = graph_general_data.ScanPathLength() # X-axis
task_success_graph_general = graph_general_data.TaskSuccess() # Y-axis
average_saccade_graph_general = graph_general_data.AverageSaccadeLength() # Hover
average_success_graph_general = graph_general_data.AverageTaskSuccess() # Line success
average_scanpath_graph_general = graph_general_data.AverageScanpathLength() # Line Scanpath


#High Scores     
high_score_tree_expert = task_success_tree_expert.max() 
high_score_tree_general = task_success_tree_general.max()
high_score_graph_expert = task_success_graph_expert.max()
high_score_graph_general = task_success_graph_general.max()
high_score_graphs = np.maximum(high_score_graph_expert,high_score_graph_general)
high_score_trees = np.maximum(high_score_tree_expert,high_score_tree_general)



# Plot
fig = go.Figure()

##################################### Traces #######################################
# graph expert trace 
fig.add_trace(
    go.Scatter(x=scanpath_graph_expert,
               y=task_success_graph_expert,
               text = average_saccade_graph_expert,
               hovertemplate=
                    "Task Success: %{y}<br>" +
                    "Scanpath: %{x:.2f}<br>" +
                    "Average Saccade Length: %{text:.2f}" +
                    "<extra></extra>",
               mode='markers',
               marker=dict(
                   size=20,
                   color='red'
               ),
               visible=True,
               name="Expert Graph"))

# graph general trace 
fig.add_trace(
    go.Scatter(x=scanpath_graph_general,
               y=task_success_graph_general,
               text = average_saccade_graph_general,
               hovertemplate=
                    "Task Success: %{y}<br>" +
                    "Scanpath: %{x:.2f}<br>" +
                    "Average Saccade Length: %{text:.2f}" +
                    "<extra></extra>",
               name="General Graph",
               mode='markers',
               marker=dict(
                   size=20,
                   color='green'
               ),
               visible=False))

# tree expert trace 
fig.add_trace(
    go.Scatter(x=scanpath_tree_expert,
               y=task_success_tree_expert,
               text = average_saccade_tree_expert,
               hovertemplate=
                    "Task Success: %{y}<br>" +
                    "Scanpath: %{x:.2f}<br>" +
                    "Average Saccade Length: %{text:.2f}" +
                    "<extra></extra>",
               mode='markers',
               marker=dict(
                   size=20,
                   color='blue'
               ),
               visible=True,
               name="Expert Tree"))

#tree general trace
fig.add_trace(
    go.Scatter(x=scanpath_tree_general,
               y=task_success_tree_general,
               text = average_saccade_tree_expert,
               hovertemplate=
                    "Task Success: %{y}<br>" +
                    "Scanpath: %{x:.2f}<br>" +
                    "Average Saccade Length: %{text:.2f}" +
                    "<extra></extra>",
               name="General Tree",
               mode='markers',
               marker=dict(
                   size=20,
                   color='purple'
               ),
               visible=False))

######################## Lines ###########################################               

# Average Success Tree General
fig.add_trace(
    go.Scatter(x=[0,2000000],
               y=[average_success_tree_general] * 15000,
               name="Average Score Tree General",
               visible=False,
               line=dict(color="purple", dash="dash")))

# Average Success Graph General
fig.add_trace(
    go.Scatter(x=[0,1700000],
               y=[average_success_graph_general] * 15000,
               name="Average Score Graph General",
               visible=False,
               line=dict(color='green', dash="dash")))

# Average Success Tree Expert
fig.add_trace(
    go.Scatter(x=[0,1700000],
               y=[average_success_tree_expert] * 15000,
               name="Average Score Tree Expert",
               visible=False,
               line=dict(color="blue", dash="dash")))

# Average Success Graph Expert
fig.add_trace(
    go.Scatter(x=[0,1700000],
               y=[average_success_graph_expert] * 15000,
               name="Average Score Graph Expert",
               visible=False,
               line=dict(color="red", dash="dash")))


# Average Scanpath Graph General
fig.add_trace(
    go.Scatter(x=[average_scanpath_graph_general] * 15000,
               y=[0,1],
               name="Average Scanpath Graph General",
               visible=False,
               line=dict(color='green', dash="dash")))

# Average Scanpath Tree General
fig.add_trace(
    go.Scatter(x=[average_scanpath_tree_general] * 15000,
               y=[0,1],
               name="Average Scanpath Tree General",
               visible=False,
               line=dict(color='purple', dash="dash")))

# Average Scanpath Graph Expert
fig.add_trace(
    go.Scatter(x=[average_scanpath_graph_expert] * 15000,
               y=[0,1],
               name="Average Scanpath Graph Expert",
               visible=False,
               line=dict(color='red', dash="dash")))

# Average Scanpath Tree Expert
fig.add_trace(
    go.Scatter(x=[average_scanpath_tree_expert] * 15000,
               y=[0,1],
               name="Average Scanpath Tree Expert",
               visible=False,
               line=dict(color='blue', dash="dash")))


# # Add Annotations and Buttons
high_annotations_expert = [dict(x="temp",
                         y=high_score_graph_expert,
                         xref="x", yref="y",
                         font=dict(
                            color="red"
                         ),
                         text="High Score Graph:<br> %.2f" % high_score_graph_expert,
                         ax=0, ay=-40),
                    dict(x="temp",
                         y=high_score_tree_expert,
                         font=dict(
                            color="blue"
                         ),
                         xref="x", yref="y",
                         text="High Score Tree:<br> %.2f" % high_score_tree_expert,
                         ax=0, ay=-40)]
high_annotations_general = [dict(x="temp",
                         y=high_score_graph_general, 
                         font=dict(
                            color="green"
                         ),
                         xref="x", yref="y",
                         text="High Score Graph:<br> %.2f" % high_score_graph_general,
                         ax=0, ay=-40),
                    dict(x="temp",
                         y=high_score_tree_expert,
                         xref="x", yref="y",
                         font=dict(
                            color="purple"
                         ),
                         text="High Score Tree:<br> %.2f" % high_score_tree_general,
                         ax=0, ay=-40)]
high_annotations_both = [dict(x="temp",
                         y=high_score_graphs, 
                         font=dict(
                            color="green"
                         ),
                         xref="x", yref="y",
                         text="High Score Graph:<br> %.2f" % high_score_graphs,
                         ax=0, ay=-40),
                    dict(x="temp",
                         y=high_score_trees,
                         font=dict(
                            color="blue"
                         ),
                         xref="x", yref="y",
                         text="High Score Tree:<br> %.2f" % high_score_trees,
                         ax=0, ay=-40)]

fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            type="buttons",
            direction="right",
            active=0,
            x=0.57,
            y=1.2,
            buttons=list([
                dict(label="Expert",
                     method="update",
                     args=[{"visible": [True, False, True, False,False,False,True,True,False,False,True,True]},
                     {"annotations": high_annotations_expert}]),
                dict(label="General",
                     method="update",
                     args=[{"visible": [False, True, False, True,True,True,False,False,True,True,False,False]},
                     {"annotations": high_annotations_general}]),
                dict(label="Both",
                     method="update",
                     args=[{"visible": [True, True, True, True,True,True,True,True,False,False,False,False]},
                     {"annotations": high_annotations_both}]),
            ]),
        )
    ])

# Set title
fig.update_layout(
    title="Participant Success and Scanpath length",
    xaxis_title="Scanpath Length",
    yaxis_title="Task Success",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="black"
    ),
    margin=dict(l=250),
)
fig.update_xaxes(range=[0,1700000])
fig.update_yaxes(range=[0,1])

offline.plot(fig,filename="Visualization.html")
fig.show()
