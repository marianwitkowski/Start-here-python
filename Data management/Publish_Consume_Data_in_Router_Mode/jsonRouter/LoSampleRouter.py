import numpy as np

class Location():
    """docstring for Location."""
    def __init__(self):
        self.lat = 0.0
        self.lon = 0.0

class SampleData():
    """docstring for SampleData."""
    def __init__(self):
        self.payload = ""
        self.temp = 0


class LoRouterData(Location):
    """docstring for ."""
    def __init__(self):
        # super(Location, self).__init__()
        self.location = Location()
        self.v = SampleData()
        self.streamId = ""
        self.timestamp = ""
        self.model = ""
        self.location.lon = 0
        self.location.lat = 0
        self.v.value = 0
        self.tags = np.chararray((3,3))
