import csv
import os
import math
import sys

test_csv = 'Data\Processed\Graph_Expert\p1.graphFXD.csv'
test_csv2 = 'Data\Processed\Graph_Expert\p3.graphFXD.csv'

Graph_Expert_Target = r"Data\Processed\Graph_Expert\\"
Graph_General_Target = r"Data\Processed\Graph_General\\"
Tree_Expert_Target = r"Data\Processed\Tree_Expert\\"
Tree_General_Target = r"Data\Processed\Tree_General\\"

Time_Interval = 60000 # one minute
One_File_Averaged = True
Start_Range = 0
End_Range = Time_Interval
# minute : [amount of people, average time for that minute]
Value_Pair = [0,0]
Participant_Counter = 0
Max_Time = 0
Min_Time = sys.maxsize

for filename in os.listdir(Graph_Expert_Target):
    with open(Graph_Expert_Target + filename, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    data = [x for x in data if x != []]
    Max_Time = max(int(data[-1][1]), Max_Time)
    Min_Time = min(int(data[-1][1]), Min_Time)

Max_Time_Minutes = math.ceil(Max_Time / Time_Interval)
Min_Time_Minutes = math.ceil(Min_Time / Time_Interval)

# Average_Dictionary = dict.fromkeys(range(1, Max_Time_Minutes + 1))
Average_Dictionary = {k: [0,0] for k in range(1, Max_Time_Minutes + 1)}

# Average_Dictionary[1] = [0,1]
# print(Average_Dictionary)
# print(Average_Dictionary[1])
# print(Average_Dictionary[1][0])
# print(Average_Dictionary[1][1])

for filename in os.listdir(Graph_Expert_Target):
    with open(Graph_Expert_Target + filename, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    data = [x for x in data if x != []]
    # increment amount of people only once
    for minute in range(1, Max_Time_Minutes + 1):
        first_time = True
        for fixation in data:
            if int(fixation[1]) < (minute * Time_Interval):
                if ((minute * Time_Interval) - Time_Interval) < int(fixation[1]) < (minute * Time_Interval):
                    # print(str(minute) + ' ' + str(fixation) + ' ' + str(minute * Time_Interval - Time_Interval))
                    # print(int(fixation[1]) + int(fixation[2]))
                    # increment the amount of people for average
                    if first_time:
                        Average_Dictionary[minute][0] += 1
                        first_time = False
                    Average_Dictionary[minute][1] += int(fixation[2])
                    print(Average_Dictionary[minute][1])
                # else:
                #     # increment the amount of people for average
                #     if first_time:
                #         Average_Dictionary[minute][0] += 1
                #         first_time = False
                #
                #     # add the fixation to current minute
                #     fixation_current = minute * Time_Interval - int(fixation[1])
                #     Average_Dictionary[minute][1] += fixation_current
                #
                #     # add portion of fixation to the next minute
                #     fixation_over = int(fixation[2]) - fixation_current
                #     new_key = minute + 1
                #     if new_key < Max_Time_Minutes:
                #         Average_Dictionary[new_key][1] = fixation_over

# with open(test_csv2, newline='') as csvfile:
#     data = list(csv.reader(csvfile))
# data = [x for x in data if x != []]
# # increment amount of people only once
# for minute in range(1, 3):
#     first_time = True
#     for fixation in data:
#         if ((minute * Time_Interval) - Time_Interval) < int(fixation[1]) < (minute * Time_Interval):
#             if (int(fixation[1]) + int(fixation[2])) < (minute * Time_Interval):
#                 print(str(minute) + ' ' + str(fixation) + ' ' + str(minute * Time_Interval - Time_Interval))
#                 print(int(fixation[1]) + int(fixation[2]))
#                 # increment the amount of people for average
#                 if first_time:
#                     Average_Dictionary[minute][0] += 1
#                     first_time = False
#                 Average_Dictionary[minute][1] += int(fixation[2])
#                 print(Average_Dictionary[minute][1])

# take average for fixation duration (should always be less than Time_Interval)
for x in range(1, Max_Time_Minutes + 1):
    if Average_Dictionary[x][0] > 0:
        Average_Dictionary[x][1] = Average_Dictionary[x][1] / Average_Dictionary[x][0] / 1000

print(Average_Dictionary)
print(Min_Time_Minutes)
