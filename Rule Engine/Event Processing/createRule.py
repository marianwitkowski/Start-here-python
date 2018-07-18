class createRule(object):
    """docstring for createRule."""
    SERVER = "https://liveobjects.orange-business.com/api/v0/"
    API_KEY = "YOUR API_KEY"
    EMAIL = "mail@gmail.com"

    def __init__(self, arg):
        super(createRule, self).__init__()
        self.arg = arg


    def createMatchingRule():
        matchingRuleId = ""
        serial="{\"dataPredicate\":{\"<\": [ {\"var\":\"value.hygrometry\"},20]},\"enabled\":true,\"name\": \"Test1211\"}";

    def main():
        matchingRuleIds = createMatchingRule()
        firingRuleId = createFiringRule(matchingRuleId)
        createActionPolicy(firingRuleId)
