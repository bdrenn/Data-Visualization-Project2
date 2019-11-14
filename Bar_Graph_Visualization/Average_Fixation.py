import csv
import os
import math
import pandas as pd
import sys

def get_Max_Time(source, Time_Interval):
    Max_Time = 0
    for filename in os.listdir(source):
        with open(source + filename, newline='') as csvfile:
            data = list(csv.reader(csvfile))
        data = [x for x in data if x != []]
        Max_Time = max(int(data[-1][1]) + int(data[-1][2]), Max_Time)
    return math.ceil(Max_Time / Time_Interval)

def mk_Average_Fixation_File(source, target, Max_Time_Minutes, Time_Interval):
    Array_Avg = []
    for row in range(Max_Time_Minutes):
        Array_Avg.append([0,0])


    for filename in os.listdir(source):
        with open(source + filename, newline='') as csvfile:
            data = list(csv.reader(csvfile))
        data = [x for x in data if x != []]
        # increment amount of people only once
        for minute in range(Max_Time_Minutes):
            first_time = True
            for fixation in data:
                if int(fixation[1]) < ((minute +1) * Time_Interval):
                    if (((minute + 1) * Time_Interval) - Time_Interval) < int(fixation[1]) < ((minute + 1) * Time_Interval):
                        if int(fixation[1]) + int(fixation[2]) < ((minute + 1) * Time_Interval):
                            # print(str(minute) + ' ' + str(fixation) + ' ' + str(minute * Time_Interval - Time_Interval))
                            # print(int(fixation[1]) + int(fixation[2]))
                            # increment the amount of people for average
                            if first_time:
                                Array_Avg[minute][0] += 1
                                first_time = False
                            Array_Avg[minute][1] += int(fixation[2])
                        else:
                            # increment the amount of people for average
                            if first_time:
                                # Average_Dictionary[minute][0] += 1
                                Array_Avg[minute][0] += 1
                                first_time = False

                            # add the fixation to current minute
                            fixation_current = (minute + 1) * Time_Interval - int(fixation[1])
                            Array_Avg[minute][1] += fixation_current

                            # add portion of fixation to the next minute
                            fixation_over = int(fixation[2]) - fixation_current
                            new_key = minute + 1
                            if new_key < Max_Time_Minutes:
                                Array_Avg[new_key][1] += fixation_over
    for x in range(Max_Time_Minutes):
        if Array_Avg[x][0] > 0:
            Array_Avg[x][1] = Array_Avg[x][1] / Array_Avg[x][0] / 1000
            # Array_Avg[x][0] = str(Array_Avg[x][0])

    print(Array_Avg)
    # with open(target, 'w') as filehandle:
    #     for listitem in Array_Avg:
    #         filehandle.write('%s\n' % listitem)

    with open(target, 'w') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(Array_Avg)

    myfile.close()
    with open(target, 'r') as file:
        lineless_target = target.replace('.csv', 'c.csv')
        with open(lineless_target, 'w') as filel:
            for line in file:
                if not line.isspace():
                    filel.write(line)


test_csv = 'Data\Processed\Graph_Expert\p1.graphFXD.csv'
test_csv2 = 'Data\Processed\Graph_Expert\p3.graphFXD.csv'

Graph_Expert_Target = r"Data\Processed\Graph_Expert\\"
Graph_General_Target = r"Data\Processed\Graph_General\\"
Tree_Expert_Target = r"Data\Processed\Tree_Expert\\"
Tree_General_Target = r"Data\Processed\Tree_General\\"

# Graph_E_target = r"data\Processed\Final\Graph_E_Final.txt"
# Graph_G_target = r"data\Processed\Final\Graph_G_Final.txt"
# Tree_E_target = r"data\Processed\Final\Tree_E_Final.txt"
# Tree_G_target = r"data\Processed\Final\Tree_G_Final.txt"

Graph_E_target = r"data\Processed\Final\Graph_E_Final.csv"
Graph_G_target = r"data\Processed\Final\Graph_G_Final.csv"
Tree_E_target = r"data\Processed\Final\Tree_E_Final.csv"
Tree_G_target = r"data\Processed\Final\Tree_G_Final.csv"

# minute : [amount of people, average time for that minute]
Time_Interval = 60000  # one minute

Max_Time_Minutes = get_Max_Time(Graph_Expert_Target, Time_Interval)
mk_Average_Fixation_File(Graph_Expert_Target, Graph_E_target, Max_Time_Minutes, Time_Interval)

Max_Time_Minutes = get_Max_Time(Graph_General_Target, Time_Interval)
mk_Average_Fixation_File(Graph_General_Target, Graph_G_target, Max_Time_Minutes, Time_Interval)

Max_Time_Minutes = get_Max_Time(Tree_Expert_Target, Time_Interval)
mk_Average_Fixation_File(Tree_Expert_Target, Tree_E_target, Max_Time_Minutes, Time_Interval)

Max_Time_Minutes = get_Max_Time(Tree_General_Target, Time_Interval)
mk_Average_Fixation_File(Tree_General_Target, Tree_G_target, Max_Time_Minutes, Time_Interval)

