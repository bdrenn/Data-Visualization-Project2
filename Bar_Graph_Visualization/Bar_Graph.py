import plotly.graph_objs as go
import pandas as pd
# import plotly.express as px
import plotly.graph_objects as go

Graph_E_target = r"data\Processed\Final\Graph_E_Finalc.csv"
Graph_G_target = r"data\Processed\Final\Graph_G_Finalc.csv"
Tree_E_target = r"data\Processed\Final\Tree_E_Finalc.csv"
Tree_G_target = r"data\Processed\Final\Tree_G_Finalc.csv"

dfGE = pd.read_csv(Graph_E_target)
dfGG = pd.read_csv(Graph_G_target)
# print(dfGE['total_people'])
print(dfGE.total_people)
# fig = go.Figure(
#     data=[go.Bar(x=dfGE['total_people'], y=dfGE['average_fixation'])],
#     layout_title_text="A Figure Displayed with fig.show()"
# )
# fig.show()

# total_people,average_fixation
# # load data
# data = []
# data_list = []
#
# with open(Graph_E_target) as f:
#     data = f.read().splitlines()
#
# for i in data:
#     removed_bracket = i[1:-1]
#     removed_space = removed_bracket.replace(' ', '')
#     list_1 = removed_space.split(",")
#     data_list.append([float(i) for i in list_1])
# print(data_list)
# x_list = list(range(1, len(data) + 1))
# print(x_list)
# y_list = [i[1] for i in data_list]
# print(y_list)
# width_list = [i[0] for i in data_list]
# width_changed = [i / 10 for i in width_list]
# print(width_changed)
# fig = go.Figure( data = [go.Bar (
#     x = x_list,
#     y = y_list,
#     width = width_changed
# )])
#
# fig.show()