import csv
import json
import os
from datetime import datetime

single_dict = { #dictionary to translate Dublin Core/GBL into GBLJson
    "Identifier":["layer_slug_s","dc_identifier_s"],
    "Provenance":["dct_provenance_s"],
    "Title":["dc_title_s"],
    "Date":["solr_year_i"],
    "Geometry Type":["layer_geom_type_s"],
    "Date Issued":["dct_issued_s"],
    "Code":["b1g_code_s"],
    "Date Accepted":["dct_dateAccepted_s"],
    "Status":["b1g_status_s"],
    "Accrual Method":["dct_accrualMethod_s"],
    "Description":["dc_description_s"],
    "Format":["dc_format_s"],
    "References":["dct_references_s"],
    "Bounding Box":["solr_geom"],
    "Centroid":["b1g_centroid_ss"]
    }
multiple_dict = {
    "Spatial Coverage":["dct_spatial_sm"],
    "Temporal Coverage":["dct_temporal_sm"],
    "Is Part Of":["dct_isPartOf_sm"],
    "Genre":["b1g_genre_sm"],
    "Subject":["dc_subject_sm"],
    "Type":["dc_type_sm"],
    "Creator":["dc_creator_sm"]
    }
if not os.path.exists("json"): #create a folder to store the jsons
    os.mkdir("json")

csvfile = open('Wi-20190807.csv', 'r')

reader = csv.DictReader(csvfile)
date_modified = datetime.today().strftime('%Y-%m-%d')+"T"+datetime.today().strftime('%X')+"Z"

for row in reader: #row is a dictionary
    small_dict = {"geoblacklight_version":"1.0","dc_rights_s":"Public","layer_modified_dt":date_modified}
    for key,val in row.items():
        if key in single_dict:
            for fieldname in single_dict[key]:
                small_dict[fieldname] = val
        if key in multiple_dict:
            for fieldname in multiple_dict[key]:
                small_dict[fieldname] = val.split('|')
    iden = row['Identifier']
    filename = iden + ".json"
    with open("json/"+filename, 'w') as jsonfile:
        json.dump(small_dict,jsonfile,indent=2)
