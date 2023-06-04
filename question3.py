# -*- coding: utf-8 -*-
"""

@author: 0002J0744

Question3.

"""

import requests
import pandas as pd


base_path = r'C:\documents\ineuron\Assignments\Git_Personal\DS_ASSIGNMENT\python'
output_file = "pokemon_data.xlsx"


url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
# Download the JSON data from the provided URL
response = requests.get(url)
data = response.json()

# Extract the desired attributes from the JSON data
attributes = [
    "id",
    "num",
    "name",
    "img",
    "type",
    "height",
    "weight",
    "candy",
    "candy_count",
    "egg",
    "spawn_chance",
    "avg_spawns",
    "spawn_time",
    "multipliers",
    "weaknesses",
    "next_evolution",
    "prev_evolution"
]

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data["pokemon"])

# Filter the DataFrame to include only the desired attributes
df = df[attributes]

# Export the DataFrame to Excel
output_file = base_path+"/pokemon_data.xlsx"
df.to_excel(output_file, index=False)

print("Excel file created successfully!")
