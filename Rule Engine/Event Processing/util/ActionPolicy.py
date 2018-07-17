import numpy as np
from Actions import Actions
from Trigger import Trigger
class ActionPolicy(Trigger,Actions):
    """docstring for actionPolicy."""
    def __init__(self,Tri,Act):
        self.enabled = False
        self.name = ""
        self.triggers = Tri
        self.actions = Act
