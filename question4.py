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
extracted_data = []

def download_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def convert_to_csv(data, filename):
   # Extract the relevant attributes from the JSON data
 
    for item in data:
        print(item.keys())
        #providing default values as in many one or other keys are missing in items
        extracted_item = {
            'Name of Earth Meteorite': item.get('name', ''),
            'Meteorite': int(item.get('id', 0)),
            'nametype': item.get('nametype', ''),
            'recclass': item.get('recclass', ''),
            'mass': float(item.get('mass', 0)) if 'mass' in item else 0.0,
            'year': item.get('year', ''),
            'reclat': float(item.get('reclat', 0.0)),
            'recclong': float(item.get('reclong', 0.0)),
            'point coordinates': item.get("geolocation", {}).get("coordinates", [])
        }
        extracted_data.append(extracted_item)
        # Write the extracted data to a CSV file
        
    with codecs.open(output_file, "w", encoding="utf-8", errors="replace") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=extracted_data[0].keys())
        writer.writeheader()
        writer.writerows(extracted_data)
    
    print(f"Data saved as {filename}")

# Main program




    
if __name__ == "__main__":
    
    url = "https://data.nasa.gov/resource/y77d-th95.json"
    data = download_data(url)
    base_path = r'C:\documents\ineuron\Assignments\Git_Personal\DS_ASSIGNMENT\python'

    output_file = base_path+"/meteorite_data2.csv"
    if data is not None:
#
        convert_to_csv(data, output_file)
    else:
        print("Failed to download the data.")
