class LoFiringRule():
    """docstring for LoFiringRule."""
    def __init__(self, name_,bool_,matchingRuleIds_,aggregationKeys_,firingType_):
        self.name = name_
        self.enabled = bool_
        self.matchingRuleIds = matchingRuleIds_
        self.aggregationKeys = aggregationKeys_
        self.firingType = firingType_
