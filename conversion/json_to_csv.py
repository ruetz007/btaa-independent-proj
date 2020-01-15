import csv
import json
import os

def jsonToCSV(json_path, csv_out_file):
    """Takes a folder of JSON files and converts them into one CSV file: one JSON file per line in the CSV"""
    
    first = True
    headers = []
    f = csv.writer(open(csv_out_file, "w", newline=''))

    for filename in os.listdir(json_path):
        if filename.endswith(".json"):
            values = []
            json_file_open = open(json_path+"\\"+filename, 'rb')
            data = json_file_open.read().decode('utf-8', errors='ignore') #ignores non-utf8 characters
            loaded = json.loads(data) #puts the json data into a dictionary
            if first: #writes the header line to the CSV
                for x in loaded:
                    headers.append(x)
                f.writerow(headers)
                first = False
            for k in headers:
                for key in loaded:
                    multiple = []
                    if key == k: #nested conditional ensures the correct value gets written under the correct header
                        if type(loaded[key]) == str:
                            values.append(loaded[key])
                        elif type(loaded[key]) == int or type(loaded[key]) == float:
                            values.append(str(loaded[key]))
                        elif type(loaded[key]) == list:
                            for y in loaded[key]:
                                multiple.append(y)
                            values.append("".join(multiple))
                        else:
                            print("something else")
            f.writerow(values) #writes the correctly-ordered values to the CSV
        else:
            print("This file is not a JSON file and will be skipped")
        json_file_open.close()