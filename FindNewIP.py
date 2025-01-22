import NewIPDetectionService

# Make sure to update this appropriately

# Last Updated at 01/22/2025 (Please keep this up to date)
oldJSONFileName = "AzureIPJsonFiles/ServiceTags_Public_20250113.json"
newJSONFileName = "AzureIPJsonFiles/ServiceTags_Public_20250120.json"

# Create DetectNewIP Object
NewIPDetector = NewIPDetectionService.IPDetector(oldJSONFileName,newJSONFileName)

# Detect New Azure Bot Service Ips
NewIPDetector.checkAzureBotService()
