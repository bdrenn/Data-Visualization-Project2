import os

class Data:

    def __init__(self,csv_file):
        self.file = csv_file

    def SaccadeLength(self):
        print("Saccade Length Array")

    def AverageSaccadeLength(self):
        print("Average Saccade Length Array")

    def ScanPathLength(self):
        print("Scanpath length array")


class GraphExpertData(Data):
    pass

class GraphGeneralData(Data):
    pass

class TreeGeneralData(Data):
    pass

class TreeExpertData(Data):
    pass
