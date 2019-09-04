import csv
import json
import os
from datetime import datetime

single_dict = { #dictionary to translate Dublin Core/GBL into GBLJson
    "Dublin Core:Identifier":["layer_slug_s","dc_identifier_s"],
    "Dublin Core:Provenance":["dct_provenance_s"],
    "Dublin Core:Title":["dc_title_s"],
    "Dublin Core:Date":["solr_year_i"],
    "GeoBlacklight:Geometry Type":["layer_geom_type_s"],
    "Dublin Core:Date Issued":["dct_issued_s"]
    }
multiple_dict = {
    "Dublin Core:Spatial Coverage":["dct_spatial_sm"],
    "Dublin Core:Temporal Coverage":["dct_temporal_sm"],
    "Dublin Core:Is Part Of":["dct_isPartOf_sm"]
    }
if not os.path.exists("json"): #create a folder to store the jsons
    os.mkdir("json")
    
csvfile = open('ArcGIS_Reaccession_20190607 - actualNew.csv', 'r')

reader = csv.DictReader(csvfile)
date_modified = datetime.today().strftime('%Y-%m-%d')

for row in reader: #row is a dictionary
    code = ""
    small_dict = {"geoblacklight_version":"1.0","dc_rights_s":"Public","layer_modified_dt":date_modified}
    for key,val in row.items():
        if key == "Code":
            code = val
            if not os.path.exists("json/" + val):
                os.mkdir("json/" + val)
        if key in single_dict:
            for fieldname in single_dict[key]:
                small_dict[fieldname] = val
        if key in multiple_dict:
            for fieldname in multiple_dict[key]:
                small_dict[fieldname] = val.split('|')
        if key == "Dublin Core:Coverage":
            val = val.split(',')
            if len(val) == 4:
                west = val[0]
                south = val[1]
                east = val[2]
                north = val[3]
                centerlat = (float(north)+float(south))/2
                centerlong = (float(east)+float(west))/2
                small_dict["solr_geom"] = "ENVELOPE("+west+","+east+","+north+","+south+")"
                small_dict["b1g_centroid_ss"] = str(centerlat) + "," + str(centerlong)
            else:
                small_dict["solr_geom"] = "NULL"
                small_dict["b1g_centroid_ss"] = "NULL"
    iden = row['Dublin Core:Identifier']
    filename = iden + ".json"
    with open("json/"+code+"/"+filename, 'w') as jsonfile:
        json.dump(small_dict,jsonfile,indent=2)
