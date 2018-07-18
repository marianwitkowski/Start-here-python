class createRule(object):
    """docstring for createRule."""
    SERVER = "https://liveobjects.orange-business.com/api/v0/"
    API_KEY = "f6422939005946619dd8a2575db3cb76"
    EMAIL = "zafnuxli@gmail.com"

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
