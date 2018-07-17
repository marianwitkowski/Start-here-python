class LoFiringReturn():
    """docstring for LoFiringReturn."""
    def __init__(self, id_,name_,bool_,matchingRuleIds_,aggregationKeys_,firingType_):
        self.id = id_
        self.name = name_
        self.enabled = bool_
        self.matchingRuleIds = matchingRuleIds_
        self.aggregationKeys = aggregationKeys_
        self.firingType = firingType_
