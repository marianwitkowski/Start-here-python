import numpy as np

class EmailAction(object):
    """docstring for EmailAction."""
    def __init__(self):
        self.to = np.chararray(())
        self.cc = np.chararray(())
        self.cci = np.chararray(())
        self.contentTemplate = ""
        self.subjectTemplate = ""
