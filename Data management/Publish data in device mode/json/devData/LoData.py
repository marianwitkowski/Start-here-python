import numpy as np

class SampleData():
    def __init__(self):
        self.payload = ""
        self.temperature = 0
        self.hygrometry = 0


class LoData(SampleData):
    """docstring for LoData."""
    def __init__(self):
        self.s = ""
        self.ts  = ""
        self.m = ""
        self.loc =  np.empty([0, 0], dtype=float)
        self.SampleData.v = null
        self.t          # optionnal tags regarding your needs
