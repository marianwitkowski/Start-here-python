import numpy as np
from Actions import Actions
from Trigger import Trigger
class ActionPolicy(object):
    """docstring for actionPolicy."""
    def __init__(self):
        self.enabled = false
        self.name = ""
        self.emails = np.chararray((3,3))
