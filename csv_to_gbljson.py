import csv
import json
import os

crosswalk_dict = { #dictionary to translate Dublin Core/GBL into GBLJson
    "Dublin Core:Identifier":["layer_slug_s","dc_identifier_s"],
    "Dublin Core:Provenance":["dct_provenance_s"],
    "Dublin Core:Title":["dc_title_s"]
    }

if not os.path.exists("json"): #create a folder to store the jsons
    os.mkdir("json")
    
csvfile = open('ArcGIS_Reaccession_20190607 - actualNew.csv', 'r')

reader = csv.DictReader(csvfile)

for row in reader: #row is a dictionary
    small_dict = {"geoblacklight_version":"1.0","dc_rights_s":"Public"}
    for key,val in row.items():
        if key in crosswalk_dict:
            for fieldname in crosswalk_dict[key]:
                small_dict[fieldname] = val
    iden = row['Dublin Core:Identifier']
    filename = iden + ".json"
    with open("json/"+filename, 'w') as jsonfile:
        json.dump(small_dict,jsonfile)
