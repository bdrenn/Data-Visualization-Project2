import os
import pandas as pd

class Data:

    def __init__(self,csv_file):
        self.data_frame = pd.read_csv(csv_file)

    def TaskSuccess(self):
        return self.data_frame.Task_Success

    def AverageSaccadeLength(self):
        return self.data_frame.saccade_length

    def ScanPathLength(self):
        return self.data_frame.scanpath

    def AverageTaskSuccess(self):
        return self.data_frame.Task_Success.mean()

    def AverageScanpathLength(self):
        return self.data_frame.scanpath.mean()


class GraphExpertData(Data):
    pass

class GraphGeneralData(Data):
    pass

class TreeGeneralData(Data):
    pass

class TreeExpertData(Data):
    pass