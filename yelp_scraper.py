# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import config
import requests
import pandas as pd
from yelpapi import YelpAPI

import numpy as np

import webbrowser

yelp_api = YelpAPI(config.api_key, timeout_s = 3.0)

df = pd.DataFrame()

#With offset parameter, can get up to 1000 business results
for offset_num in range(0, 1000, 20):
    search_results = yelp_api.search_query(term = 'dinner', location = 'Fairfax, VA', radius = 11265, sort_by = 'rating', offset=offset_num)
    temp_df = pd.DataFrame(search_results['businesses'])
    df = df.append(temp_df, ignore_index=True)
    

#Filter out address so easily accessible
df['address'] = df['location'].apply(lambda x: x['display_address'])

#Add state, city, zipcode (easily filterable)
df['state'] = df['address'].apply(lambda x: x[-1].split(', ')[1].split(' ')[0])
df['city'] = df['address'].apply(lambda x: x[-1].split(', ')[0])
df['zip_code'] = df['address'].apply(lambda x: x[-1].split(', ')[1].split(' ')[-1])

#Filter out categories
df['genre'] = df['categories'].apply(lambda x: [ele['title'] for ele in x])

#Categories split up
cat_df = pd.DataFrame(df['genre'].to_list(), columns=['category1', 'category2', 'category3'])                 
df = pd.concat([df, cat_df], axis=1)

#Transactions split up
transactions_df = pd.DataFrame(df['transactions'].to_list(), columns = ['transactions1', 'transactions2', 'transactions3'])
df = pd.concat([df, transactions_df], axis=1)

#Verify cities
df_city = df['city'].value_counts()

df.to_csv('Fairfax_VA_dinner_7mi.csv')

#Convert Tyson's/Mc Lean/Mclean to just McLean for simplicity
mclean_list = ['Tysons', 'Tysons Corner', 'Mclean', "Tyson's Corner-Vienna", 'Mc Lean']
df['city'] = df['city'].apply(lambda x: 'McLean' if x in mclean_list else x)

#Filter only for review counts > 50 (realize I may be missing some gems but that's how it goes)
df_50 = df[df['review_count'] > 50]

#Filter for VA only
df_50_VA = df_50[df_50['state'] == 'VA']

#Filter for 4.5 and up
df2 = df_50_VA[df_50_VA['rating'] > 4.0]

#Attempt to get value_counts
df_cat = df2[['category1', 'category2', 'category3']].apply(pd.value_counts).sum(axis=1).astype(int)




def find_category(df, categories):
    '''Filter out rows that contain list of categories
    Input:
    df = dataframe
    categories = list of categories
    '''
    return_df = pd.DataFrame()
    for category in categories:
        temp_df = df[(df['category1']==category) | (df['category2'] == category) | (df['category3'] == category)]
        return_df = pd.concat([return_df, temp_df])
    return return_df.groupby(return_df.index).first() #Remove duplicate entries


df_alcohol = find_category(df2, ['Cocktail Bars', 'Whiskey Bars', 'Wine Bars'])
alcohol_url = df_alcohol['url']

for url in alcohol_url:
    webbrowser.open(url)
