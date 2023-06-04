# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 03:03:38 2023

@author: 0002J0744
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
url = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"
data = pd.read_csv(url)

data.to_csv('car.csv')

# Get all TESLA cars with the model year and model made in Bothell City
tesla_bothell = data[(data['Make'] == 'TESLA') & (data['City'] == 'Bothell')]
print("TESLA cars with the model year and model made in Bothell City:")
print(tesla_bothell)
print()

# Get all the cars that have an electric range of more than 100 and were made after 2015
electric_range_100 = data[(data['Electric Range'] > 100) & (data['Model Year'] > 2015)][['Make', 'Model']]
print("Cars that have an electric range of more than 100 and were made after 2015:")
print(electric_range_100)
print()

# Draw plots to show the distribution between city and electric vehicle type
plt.figure(figsize=(12, 6))
data_filtered = data[data['Electric Vehicle Type'] == 'Electric']
ax = data_filtered['City'].value_counts().plot(kind='bar', color='skyblue')
ax.set_title('Distribution of Electric Vehicle Type by City')
ax.set_xlabel('City')
ax.set_ylabel('Count')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
