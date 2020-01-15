import os
import json_to_csv as jtc
import csv_to_gbljson as ctj


def toCSV():
    """Uses the json_to_csv module to convert JSONs to a CSV. Error checking ensures correct function parameters"""
    
    file_path = input("Please input the path to the folder of JSONs: ")
    while not os.path.exists(file_path):
        print("Path does not exist. Please try again.")
        file_path = input("Please input the path to the folder of JSONs: ")
    
    file_name = input("Please give the desired name of the output CSV: ")
    while not file_name.endswith(".csv"):
        print("File name must end with .csv")
        file_name = input("Please give the desired name of the output CSV: ")
    
    jtc.jsonToCSV(file_path, file_name)
    print("JSONs have been converted to a CSV")
    
def toJSON():
    """Uses the csv_to_gbljson module to convert a CSV to JSONs. Error checking ensures correct function parameters"""
    file_path = input("Please input the path to the CSV to convert: ")
    while not os.path.exists(file_path):
        print("Path does not exist. Please try again.")
        file_path = input("Please input the path to the CSV to convert: ")
        
    ctj.csvToJson(file_path)
    print("CSV has been converted to JSONs. Look in your current directory for a folder named 'json'")
    
def main():
    """Users picks which task they want to run"""
    
    task = input("Type c to convert jsons to a csv, or type j to convert a csv into geojsons: ")
    task = task.lower()
    while(task != "c" and task != "j"):
        task = input("Invalid input. Type c to convert jsons to a csv, or type j to convert a csv into geojsons: ")
        task = task.lower()
    if(task == "c"):
        toCSV()
    if(task == "j"):
        toJSON()
    
if __name__ == "__main__":
    main()