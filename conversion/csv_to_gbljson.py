import csv
import json
import os
from datetime import datetime

single_dict = { #dictionary to translate single-value Dublin Core/GBL fields into GBLJson
    "Identifier":["layer_slug_s","dc_identifier_s"],
    "Status":["b1g_status_s"],
    "Code":["b1g_code_s"],
    "Date Accessioned":["b1g_dateAccessioned_s"],
    "Date Retired":["b1g_dateRetired_s"],
    "Suppressed":["suppressed_b"],
    "Accrual Method":["dct_accrualMethod_s"],
    "Title":["dc_title_s"],
    "Description":["dc_description_s"],
    "Date Issued":["dct_issued_s"],
    "Solr Year":["solr_year_i"],
    "Provenance":["dct_provenance_s"],
    "Format":["dc_format_s"],
    "Geometry Type":["layer_geom_type_s"],
    "Image":["b1g_image_ss"],
    "Layer ID":["layer_id_s"],
    "References":["dct_references_s"],
    "Bounding Box":["solr_geom"]
    }
multiple_dict = { #dictionary to translate multivalue Dublin Core/GBL fields into GBLJson
    "Is Part Of":["dct_isPartOf_sm"],
    "Alternative Title":["dct_alternativeTitle_sm"],
    "Genre":["b1g_genre_sm"],
    "Subject":["dc_subject_sm"],
    "Keyword":["b1g_keyword_sm"],
    "Temporal Coverage":["dct_temporal_sm"],
    "Spatial Coverage":["dct_spatial_sm"],
    "Publisher":["dc_publisher_sm"],
    "Creator":["dc_creator_sm"],
    "Language":["dc_language_sm"],
    "Type":["dc_type_sm"],
    "Geonames":["b1g_geonames_sm"]
    }
    
def csvToJson(csv_file):
    """Takes an input CSV file, converts each line of the CSV into a geoJSON file, and stores the geoJSONs in a directory"""
    
    if not os.path.exists("WIjson"): #create a folder to store the jsons if one does not already exist
        os.mkdir("WIjson")
        
    csvfile = open(csv_file, 'r') #opens the csv with the GBL data

    reader = csv.DictReader(csvfile)
    date_modified = datetime.today().strftime('%Y-%m-%d') #sets date modified to the current date

    for row in reader: #each row is a dictionary
        code = ""
        ref = []
        small_dict = {"geoblacklight_version":"1.0","dc_rights_s":"Public","layer_modified_dt":date_modified} #starting dictionary with set values
        for key,val in row.items():
            print(key)
            if key == "Code":
                code = val
                if not os.path.exists("WIjson/" + val): #makes a new folder for each code
                    os.mkdir("WIjson/" + val)
            if key in single_dict:
                for fieldname in single_dict[key]:
                    small_dict[fieldname] = val
            if key in multiple_dict:
                for fieldname in multiple_dict[key]:
                    small_dict[fieldname] = val.split('|') #creates a list with the multiple values
            #if key == "Bounding Box":
            #    val = val.split(',')
            #    if len(val) == 4: #takes care of bounding box values and calculates centroid
            #        west = val[0]
            #        south = val[1]
            #        east = val[2]
            #        north = val[3]
            #        centerlat = (float(north)+float(south))/2
            #        centerlong = (float(east)+float(west))/2
            #        small_dict["solr_geom"] = "ENVELOPE("+west+","+east+","+north+","+south+")"
            #        small_dict["b1g_centroid_ss"] = str(centerlat) + "," + str(centerlong)
            #    else: #if the bounding box doesn't have all coordinates, just write values as null
            #        small_dict["solr_geom"] = "NULL"
            #        small_dict["b1g_centroid_ss"] = "NULL"
            if key == "Information" and val != '':
                to_append = '"http://schema.org/url":"' + val + '"'
                ref.append(to_append)
            if key == "Download" and val != '':
                to_append = '"http://schema.org/downloadUrl":"' + val + '"'
                ref.append(to_append)
            if key == "MapServer" and val != '':
                to_append = '"urn:x-esri:serviceType:ArcGIS#DynamicMapLayer":"' + val + '"'
                ref.append(to_append)
            if key == "FeatureServer" and val != '':
                to_append = '"urn:x-esri:serviceType:ArcGIS#FeatureLayer":"' + val + '"'
                ref.append(to_append)
            if key == "ImageServer" and val != '':
                to_append = '"urn:x-esri:serviceType:ArcGIS#ImageMapLayer":"' + val + '"'
                ref.append(to_append)
            if key == "ISO Metadata" and val != '':
                to_append = '"http://www.isotc211.org/schemas/2005/gmd/":"' + val + '"'
                ref.append(to_append)
            if key == "FGDC Metadata" and val != '':
                to_append = '"http://www.opengis.net/cat/csw/csdgm":"' + val + '"'
                ref.append(to_append)
            if key == "WFS" and val != '':
                to_append = '"http://www.opengis.net/def/serviceType/ogc/wfs":"' + val + '"'
                ref.append(to_append)
            if key == "WMS" and val != '':
                to_append = '"http://www.opengis.net/def/serviceType/ogc/wms":"' + val + '"'
                ref.append(to_append)
            if key == "HTML" and val != '':
                to_append = '"http://www.w3.org/1999/xhtml":"' + val + '"'
                ref.append(to_append)
            if key == "IIIF" and val != '':
                to_append = '"http://iiif.io/api/image":"' + val + '"'
                ref.append(to_append)
            if key == "Manifest" and val != '':
                to_append = '"http://iiif.io/api/presentation#manifest":"' + val + '"'
                ref.append(to_append)
            if key == "IndexMaps" and val != '':
                to_append = '"https://openindexmaps.org":"' + val + '"'
                ref.append(to_append)
        #small_dict["dct_references_s"] = '{' + (','.join(ref)) + '}'
        iden = row['Identifier']
        filename = iden + ".json"
        with open("WIjson/"+code+"/"+filename, 'w') as jsonfile: #writes to a json with the identifier as the filename
            json.dump(small_dict,jsonfile,indent=2)
