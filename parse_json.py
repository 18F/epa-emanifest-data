import json
from pprint import pprint

with open('data/manifestsample.json') as data_file:
    data = json.load(data_file)


#pprint(data)


#print(len(data))
"""
Data is only 1 object in a list. Why?
Is this being manually generated? If so, why? While this is valid, it is not logical.
"""

data = data[0]  # Pull the first item out.

for item in data:
    #pprint(item)

    """
    Keys
    ['Generator', 'InternationalShipmentInfo', 'TSDF',
        'EmergencyResponsePhone', 'DesignatedFacilityInfo',
        'ManifestTrackingNumber', 'Transporter', 'ManifestedWaste',
        'AdditionalInfo_Line14']
    """

    for value in data[item]:
        #pprint(type(value))
        """ Values are strings or dicts """

        print(item, value)



