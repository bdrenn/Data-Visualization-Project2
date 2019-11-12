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

#Data Object 
graph_expert_data = Data.GraphExpertData(graph_expert_data_dir)
array = graph_expert_data.ScanPathLength()
print(array)





