#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:58:02 2020

Opens x url links of 4.5 ratings or better on yelp.
This script has my client_id and api_key but 

@author: daniellim
"""
#Next steps:
#Enter a way for filtering out $, $$, $$$, $$$$


import pandas as pd
from yelpapi import YelpAPI
import config
import webbrowser

yelp_api = YelpAPI(config.api_key, timeout_s = 10.0)

term = input('Enter search term: ')
location = input('Enter location: ')
radius = int(int(input('Enter mile radius search (Max 25): '))*1609.34)
search_num = int(input('Enter number of searches (Max 1000): '))
min_ratings = int(input('Enter minimum amount of ratings for establishment: '))
browser_yn = input('Open some results in browser? y for yes n for no: ')
window_num = int(input('Enter how many results you would like displayed: '))

df = pd.DataFrame()

for offset_num in range(0, search_num, 20):
    search_results = yelp_api.search_query(term = term, location = location, radius = radius, sort_by = 'rating', offset=offset_num)
    temp_df = pd.DataFrame(search_results['businesses'])
    df = df.append(temp_df, ignore_index=True)

df = df[df['review_count'] > (min_ratings)]
df = df[df['rating'] > 4.0]

if browser_yn == 'y':
    for url in df['url'].head(window_num):
        webbrowser.open(url, new=1)

df.to_csv(f'{location} {term}.csv')

