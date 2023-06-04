# -*- coding: utf-8 -*-
"""

@author: Amritesh

Question 4 -
Write a program to download the data from the link given below and then read the data and convert the into
the proper structure and return it as a CSV file.
Link - https://data.nasa.gov/resource/y77d-th95.json
Note - Write code comments wherever needed for code understanding.
Sample Data -
Excepted Output Data Attributes
● Name of Earth Meteorite - string id - ID of Earth
● Meteorite - int nametype - string recclass - string
● mass - Mass of Earth Meteorite - float year - Year at which Earth
● Meteorite was hit - datetime format reclat - float recclong - float
● point coordinates - list of int

"""

import requests
import csv
import codecs

def download_and_convert_data(url, output_file):
    # Download the JSON data from the provided URL
    response = requests.get(url)
    data = response.json()

    # Extract the desired attributes from the JSON data
    attributes = [
        "name",
        "id",
        "nametype",
        "recclass",
        "mass (g)",
        "year",
        "reclat",
        "reclong",
        "geolocation"
    ]

    # Write the data to a CSV file
    with codecs.open(output_file, "w", encoding="utf-8", errors="replace") as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header row
        writer.writerow(attributes)
        
        # Write each meteorite's data as a row in the CSV file
        for meteorite in data:
            row = [
                meteorite.get("name", ""),
                meteorite.get("id", ""),
                meteorite.get("nametype", ""),
                meteorite.get("recclass", ""),
                meteorite.get("mass (g)", ""),
                meteorite.get("year", ""),
                meteorite.get("reclat", ""),
                meteorite.get("reclong", ""),
                meteorite.get("geolocation", {}).get("coordinates", [])
            ]
            writer.writerow(row)

    print("CSV file created successfully!")


    
if __name__ == "__main__":
    
    base_path = r'C:\documents\ineuron\Assignments\Git_Personal\DS_ASSIGNMENT\python'
    
    url = "https://data.nasa.gov/resource/y77d-th95.json"
    output_file = base_path+"/meteorite_data.csv"
    download_and_convert_data(url, output_file)
