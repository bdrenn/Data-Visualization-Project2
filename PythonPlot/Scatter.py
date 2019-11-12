import plotly.graph_objects as go
import numpy as np
import os 
import Preprocess as Data

output_data_dir = os.getcwd() + '/OutputData'

graph_expert_data_dir = output_data_dir + '/GraphExpertData.csv'
graph_expert_data = Data.GraphExpertData(graph_expert_data_dir)
graph_expert_data.SaccadeLength()


