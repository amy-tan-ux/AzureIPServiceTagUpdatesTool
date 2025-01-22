import json

# DetectNewIP compares 2 JSON and checks for changes and update to the JSON
class IPDetector:
    
    def __init__ (self, oldJsonName, newJsonName):

        # Read Json
        with open(oldJsonName, 'r') as oldFile:
            self.oldJson = json.load(oldFile)
        with open(newJsonName, 'r') as newFile:
            self.newJson = json.load(newFile)

    def checkAzureBotService(self):
        
        oldIps = []
        newIps = []

        for listOfOldIps in self.oldJson.get("values"):
            if listOfOldIps.get("id") == "AzureBotService":
                oldIps = listOfOldIps.get("properties").get("addressPrefixes")
        for listOfNewIps in self.newJson.get("values"):
            if listOfNewIps.get("id") == "AzureBotService":
                newIps = listOfNewIps.get("properties").get("addressPrefixes")
                
        ipsToAdd = []

        for n_ip in newIps:
            if n_ip not in oldIps:
                ipsToAdd.append(n_ip)
            else: 
                oldIps.remove(n_ip)

        print ("Please add the following Azure Bot Serice IPs")
        print(n_ip) # List of new Azure Bot Service Ips added that need whitelisting
        
        if oldIps:
            print ("Please remove the following Azure Bot Service Ips")
            print (oldIps) # List of unused Azure Bot Service Ips that should be removed


