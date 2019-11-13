import csv
import os

def txt_to_csv(source, target):
    in_txt = csv.reader(open(source, "rt"), delimiter='\t')
    out_csv = csv.writer(open(target, 'wt'))
    out_csv.writerows(in_txt)


# convert files to csv

Graph_Expert_Directory = r"Data\Unprocessed\Graph_Expert\\"
Graph_General_Directory = r"Data\Unprocessed\Graph_General\\"
Tree_Expert_Directory = r"Data\Unprocessed\Tree_Expert\\"
Tree_General_Directory = r"Data\Unprocessed\Tree_General\\"

Graph_Expert_Target = r"Data\Processed\Graph_Expert\\"
Graph_General_Target = r"Data\Processed\Graph_General\\"
Tree_Expert_Target = r"Data\Processed\Tree_Expert\\"
Tree_General_Target = r"Data\Processed\Tree_General\\"

# only take files ending with FXD
suffix = 'FXD.txt'
for filename in os.listdir(Graph_Expert_Directory):
    if filename.endswith(suffix):
        txt_to_csv(Graph_Expert_Directory + filename, (Graph_Expert_Target + filename).replace('txt', 'csv'))
for filename in os.listdir(Graph_General_Directory):
    if filename.endswith(suffix):
        txt_to_csv(Graph_General_Directory + filename, (Graph_General_Target + filename).replace('txt', 'csv'))

for filename in os.listdir(Tree_Expert_Directory):
    if filename.endswith(suffix):
        txt_to_csv(Tree_Expert_Directory + filename, (Tree_Expert_Target + filename).replace('txt', 'csv'))
for filename in os.listdir(Tree_General_Directory):
    if filename.endswith(suffix):
        txt_to_csv(Tree_General_Directory + filename, (Tree_General_Target + filename).replace('txt', 'csv'))