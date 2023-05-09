#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 22:23:56 2023

@author: mpgeiss
"""
import pandas as pd
import fiona
import numpy as np
import json
import seaborn as sns
import requests
import geopandas as gpd
import matplotlib.pyplot as plt

import requests


#read in site-related USGS groundwater data 
sites = pd.read_csv("sites.csv")

#use nominatim API to get ZIP codes per site location
def get_zip_code(Lat, Long):
# Set up the API endpoint
    endpoint = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "format": "json",
        "lat": Lat,
        "lon": Long,
        "zoom": 18,
        "addressdetails": 1
    }
    #read ZIP codes for sites into dataframe
    response = requests.get(endpoint, params=params)
    if response.ok:
        data = response.json()
        # Extract the zip code from the API response
        zip_code = data.get('address', {}).get('postcode', None)
        return zip_code
    
    else:
       # Handle API request error
       print(f"Error getting zip code for lat={Lat}, lon={Long}")
       return None
#add ZIP code column into sites df
sites['Zip Code'] = sites.apply(lambda row: get_zip_code(row['Lat'], row['Long']), axis=1)
#print(sites.columns)

#write new CSV w/zip data
sites.to_csv('sites w zip.csv')

key_columns = ['Pharmaceuticals ', 'Pesticides', 'PCHC', 'Total.TPs']

#calculate median []'s for each compound type across all sites
medians = sites.groupby('Zip Code')[key_columns].median()

#create new csv with median []'s for each compound type
medians.to_csv('median agg concentrations per zip.csv')

zip_demos = pd.read_csv('suff_demograhs.csv')

#for v in sites['Zip Code']:
    
    

#easier -> block-group data. get some. add water/sewer #s.
#census pull data
#pull populations per zip code...


api = 'https://api.census.gov/data/2018/acs/acs5'

key_value =  "97f60f44aa5b7ef48a4526b5b25efa11d58f6d99"

for_clause = "zip code tabulation area:*"
in_clause = "state:36"

variables = {'B02001_001E':'pop_total', 'B02001_002E':'pop_white', 
             'B25003_001E':'housing_total', 'B25003_002E':'housing_owned', 'B25003_003E':'housing_rental', 
             'B01001_001E': 'total_population', "B02002_001E": 'median_earnings'}
# '...': 'median_income', '...': 'educational_attainment'


key_list= 'Name, B02001_001E, B02001_002E, B25003_001E, B25003_002E, B25003_003E, B01001_001E, B20002_001E' #'...', '...'

#pull request issue...
var_string = 'NAME, B02001_001E,B02001_002E,B25003_001E,B25003_002E,B25003_003E, B01001_001E'

var_list= ['B02001_001E','B0200p1_002E',
           'B25003_001E','B25003_002E','B25003_003E', 'B01001_001E','B02002_001E' ]

#retrieve income data from API
payload = {'get':'B20002_001E', 'for': for_clause, 'in': in_clause,'key': key_value}

response = requests.get(api, payload)
if response.status_code == 200:
    print("API pull request for Census data succeeded!")

else: 
    print(response.status_code)
    print(response.text)
    assert False 

row_list = response.json()
colnames = row_list[0]
datarows = row_list[1:]
income= pd.DataFrame(columns=colnames, data=datarows)

income['median'] = income['B20002_001E'].astype(float)
income = income.replace("-666666666", np.nan)

#csv with median income information per zip code
income.to_csv("median_income_per_zip.csv", index = False)

#2nd Census API request for total population, instead of median income, per zip code

payload = {'get':'B01001_001E', 'for': for_clause, 'in': in_clause,'key': key_value}

response = requests.get(api, payload)
if response.status_code == 200:
    print("API pull request for Census data succeeded!")

else: 
    print(response.status_code)
    print(response.text)
    assert False 

row_list = response.json()
colnames = row_list[0]
datarows = row_list[1:]
population= pd.DataFrame(columns=colnames, data=datarows)

income['tot_population'] = population['B01001_001E']


medians['tot_population'] = population['B01001_001E']
medians['income'] = income['median']

medians.to_csv("demographics_per_zip.csv", index= False)
#isolated csv for population per zip code

payload = {'get':'NAME,B01001_001E', 'for': for_clause, 'in': in_clause,'key': key_value}

response = requests.get(api, payload)
if response.status_code == 200:
    print("API pull request for Census data succeeded!")

else: 
    print(response.status_code)
    print(response.text)
    assert False 

row_list = response.json()
colnames = row_list[0]
datarows = row_list[1:]
pop= pd.DataFrame(columns=colnames, data=datarows)


pop.to_csv("pop_per_zip.csv", index = False)







