import csv
import json
import os

os.mkdir("json")
csvfile = open('ArcGIS_Reaccession_20190607 - actualNew.csv', 'r')
#jsonfile = open('file.json', 'w')

crosswalk_dict = {"Dublin Core:Identifier":["layer_slug_s","dc_identifier_s"]}
                  

fieldnames = ("layer_slug_s","geoblacklight_version","dct_provenance_s","dc_title_s","dc_rights_s","dc_identifier_s")
reader = csv.DictReader(csvfile)

for row in reader: #row is a dictionary
    #print row
    iden = row['Dublin Core:Identifier']
    filename = iden + ".json"
    jsonfile = open("json/"+filename, 'w')
    json.dump(row,jsonfile)
    

#filter_dict = {}
#for key,val in reader.items():
#    if key is in crosswalk_dict:
#        filter_dict

#out = json.dump( [ row for row in reader ], jsonfile )
#jsonfile.write(out)
