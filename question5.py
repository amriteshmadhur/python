# -*- coding: utf-8 -*-
"""

@author: Amritesh
"""

import requests
import html2text

# Send a GET request to retrieve the show data
response = requests.get('http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes')
show_data = response.json()

# Extract and process episode data
episodes = show_data['_embedded']['episodes']
for episode in episodes:
    episode_id = episode['id']
    episode_url = episode['url']
    episode_name = episode['name']
    season_number = episode['season']
    episode_number = episode['number']
    episode_type = episode['type']
    airdate = episode['airdate']
    airtime = episode['airtime']
    runtime = episode['runtime']
    average_rating = episode['rating']['average']
    summary = html2text.html2text(episode['summary'].replace('<p>', '').replace('</p>', ''))
    medium_image_link = episode['image']['medium']
    original_image_link = episode['image']['original']

    # Print the extracted data with proper formatting
    print("Episode ID: ", episode_id)
    print("URL: ", episode_url)
    print("Name: ", episode_name)
    print("Season: ", season_number)
    print("Number: ", episode_number)
    print("Type: ", episode_type)
    print("Airdate: ", airdate)
    print("Airtime: ", airtime)
    print("Runtime: ", runtime)
    print("Average Rating: ", average_rating)
    print("Summary: ", summary)
    print("Medium Image Link: ", medium_image_link)
    print("Original Image Link: ", original_image_link)
    print("\n")
