# AzureIPServiceTagUpdatesTool
Azure Service Ips are always changing ( resources: https://www.microsoft.com/en-us/download/details.aspx?id=56519). This project compares the old list of IPs provided by this documentation and the new ones and returns which ip needs to be added or removed. 

# Detect New Ips Added to ServiceTags JSON 

The Service Tags Json files provided by Microsoft here: https://www.microsoft.com/en-us/download/details.aspx?id=56519

The Json lists all Ips used to host Azure Services. New Ips will be added 1 week before it is launched so it gives us 1 week of time to whitelist and make changes accordingly

Run FindNewIP to get all ips that have been added or removed by Microsoft

# How to use FindNewIP

FindNewIP utilizes NewIPDetectionService to read the json files you download from the microsoft site here:https://www.microsoft.com/en-us/download/details.aspx?id=56519

1. Add the new and old Json file inside the AzureIPJSONFiles File (the old one would already be saved here).
2. Update the values to oldJSONFileName and newJSONFileName inside FindNewIP.py
3. Save and Run
