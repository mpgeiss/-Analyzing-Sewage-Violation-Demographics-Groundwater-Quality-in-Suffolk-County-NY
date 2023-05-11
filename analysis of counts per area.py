#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:08:14 2023

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
plt.rcParams["figure.dpi"] = 300
#read in zipcode boundaries
zipcodes = gpd.read_file('suff_zips.gpkg', layer = 'suffolk_zips')


#read in zip code demographics
zip_demos = pd.read_csv('suff_demographics_zip.csv')

zip_demos = zip_demos.drop(zip_demos.columns[4:], axis=1)

print(zip_demos)

med_income = zip_demos['Median_Income']

#calculate geopgrahic area per zip code

zipcodes['area'] = zipcodes.geometry.area
area_by_zipcode = zipcodes.groupby('ZCTA5CE10')['area'].sum() * 1000
 
#read in land use boundaries
land_use =  gpd.read_file('Land_Use_2016_Polygon.zip')

#read in WWTP locations:
WWTPs =   gpd.read_file('WWTPs.gpkg', layer = 'wwtps_in_suffolk')

Centroids = pd.read_csv("NYS-Tax-Parcel-Centroid-Points.gdb.zip") 

#read in centroids
sewers = gpd.read_file('sewers.gpkg', layer = 'sewers')

OWTS = gpd.read_file('OWTS.gpkg', layer = 'owts_props')

#dissolve land-uses into distinct polygons
land_dissolve = land_use.dissolve(by='DESCRIPTIO', as_index=False)

#calculate area of each land-use type
land_dissolve['area'] =land_dissolve.geometry.area

land_dissolve_reproj =  land_dissolve.to_crs(epsg=4326)
sum_ = land_dissolve_reproj.area.sum()

#write land use dissolved layer to a file

land_dissolve.to_file('dissolved_land_uses.shp')

print("sewers", sewers.crs)
print("land_dissolve", land_dissolve.crs)
print(WWTPs.crs)

#set sewer & OWTS layers to same crs as the land_use dissolve layer
sewers = sewers.to_crs(4326)
OWTS = OWTS.to_crs(4326)

#land_dissolve = land_dissolve.to_crs(26918)

#set same crs:
    
 #left-join land-uses onto points  with a for-lop for sewer, OWTS< WWTP locations
 
join = sewers.sjoin(land_dissolve, how="left", predicate="within")

#count # of parcels with sewage connections per land use type
join = join['DESCRIPTIO'].value_counts(dropna=False)

join = pd.DataFrame(join)

join= join.rename(columns={'DESCRIPTIO': 'sewage_connections_BY_LAND_USE', '' : 'Land-Use'})

#calculate the share of sewage connections, for each land use type, by all parcels with sewage conections

join['share'] = 100* join['sewage_connections_BY_LAND_USE']/sum(join['sewage_connections_BY_LAND_USE'])

join['DESCRIPTIO'] = ['Medium Density Residential', 'Low Density Residential', 'High Density Residential',                               
                      'Commercial', 'Vacant', 'Preserved Recreation and Open Space', 'Institutional', 'Industrial',
                      'Agriculture', 'Transportation', 'Utilities', 'Surface Waters', 'NaN', 'Waste Handling and Mangement']                                     
    

join.to_csv("sewers_per_landuse.csv")
#for WWTPS PER TYPE OF LAND USE:
join_2 = WWTPs.sjoin(land_dissolve, how="left", predicate="within")
join_2 = join_2['DESCRIPTIO'].value_counts(dropna=False)

join_2 = pd.DataFrame(join_2)
join_2= join_2.rename(columns={'DESCRIPTIO': 'WWTPs_BY_LAND_USE', '' : 'Land-Use'})
join_2['share'] = 100* join_2['WWTPs_BY_LAND_USE']/sum(join_2['WWTPs_BY_LAND_USE']) 

#calculate # of WWTPs by area for a 'density' measure

join_2['WWTPs_BY_LAND_USE density'] = join_2['WWTPs_BY_LAND_USE']/land_dissolve['area']


join_2['DESCRIPTIO'] = ['High Density Residential','Waste Handling and Mangement', 'Commercial', 'Institutional',           
                        'Preserved Recreation and Open Space','Industrial', 'Utilities','Transportation', 'Medium Density Residential', 'Vacant','NaN',
                        'Agriculture','Low Density Residential']                            

join_2.to_csv("WWTPs by land-use.csv")

#for #OWTS properties PER TYPE OF LAND USE:
join_3 = OWTS.sjoin(land_dissolve, how="left", predicate="within")
join_3 = join_3['DESCRIPTIO'].value_counts(dropna=False)


join_3 =  pd.DataFrame(join_3)
join_3 = join_3.rename(columns={'DESCRIPTIO': 'OWTS_BY_LAND_USE', '' : 'Land-Use'})
join_3['share'] = 100* join_3['OWTS_BY_LAND_USE']/sum(join_3['OWTS_BY_LAND_USE'])
join_3['DESCRIPTIO'] = ['Preserved Recreation and Open Space', 'Vacant','Medium Density Residential', 
                        'Low Density Residential', 'Agriculture', 'High Density Residential',
                        'Transportation','Surface Waters', 'Commercial', 'Utilities',
                        'Industrial', 'Institutional', 'NaN','Waste Handling and Mangement']                        
join_3.to_csv("OWTS PROPERTIES by land-use.csv")

#join all 3 attrbiutes per land-use into 1 df

merge_land = join.merge(join_2, on = 'Land-Use').merge(join_3, on = 'Land-Use')

#count sewer points per zip code
sewers_per_zip = sewers.sjoin(zipcodes, how="left", predicate="within")
sewers_per_zip = sewers_per_zip['ZCTA5CE10'].value_counts(dropna = False)
sewers_per_zip = pd.DataFrame(sewers_per_zip) 
#calculate relative density of sewers per zip!
sewers_per_zip['sewer_density'] = sewers_per_zip['ZCTA5CE10']/area_by_zipcode



sewers_per_zip.to_csv('sewers_per_zip.csv')



#combine information into 1 land-use file:


#count OWTS sides by zip
OWTS_per_zip = OWTS.sjoin(zipcodes, how="left", predicate="within")
OWTS_per_zip = OWTS_per_zip['ZCTA5CE10'].value_counts(dropna = False)
OWTS_per_zip = pd.DataFrame(OWTS_per_zip)
OWTS_per_zip['sewer_density'] = OWTS_per_zip['ZCTA5CE10']/area_by_zipcode

OWTS_per_zip.to_csv('OWTS_per_zip.csv')



#Count WWTPs per zip code: 
WWTPs_per_zip = WWTPs.sjoin(zipcodes, how="left", predicate="within")
WWTPs_per_zip = WWTPs_per_zip['ZCTA5CE10'].value_counts(dropna = False)

WWTPs_per_zip = pd.DataFrame(WWTPs_per_zip) 
WWTPs_per_zip['sewer_density'] = WWTPs_per_zip['ZCTA5CE10']/area_by_zipcode
WWTPs_per_zip.to_csv('WWTPs_per_zip.csv')   



#add zip-information to zip infor file:
zip_inf = pd.read_csv("demographics_per_zip.csv")   

#make interesting plots about properties with septic systems: 
    
fig, ax = plt.subplots()
ax.barh(join_3['DESCRIPTIO'],join_3['share'])

ax.set_ylabel('Land-Use Category')
ax.set_xlabel('For all septic system parcels, % share')

plt.show()
fig.tight_layout()
fig.savefig(f"For all septic system properties, share by land-use.png")


#same plot as above, with raw counts
fig, ax = plt.subplots()
ax.barh(join_3['DESCRIPTIO'],join_3['OWTS_BY_LAND_USE'])

ax.set_ylabel('Land-Use Category')
ax.set_xlabel('# Documented Parcels with Septic System')

plt.show()
fig.tight_layout()
fig.savefig(f"Septic system share raw # by land-use.png")


#FOR SEWAGE CONNECTS: plot about attributes
fig, ax = plt.subplots()
ax.barh(join['DESCRIPTIO'],join['share'])

ax.set_ylabel('Land-Use Category')
ax.set_xlabel('% of Documented Parcel Sewage Connections')

plt.show()
fig.tight_layout()
fig.savefig(f"sewer share raw # by land-use.png")


fig, ax = plt.subplots()
ax.barh(join_2['DESCRIPTIO'],join_2['share'])

ax.set_ylabel('Land-Use Category')
ax.set_xlabel('% of WWTPs in Suffolk County')

plt.show()
fig.tight_layout()
fig.savefig(f"OWTS share raw # by land-use.png")





#plot of income vs sewage count density per zip
sewers_per_zip = sewers_per_zip.rename(columns={'ZCTA5CE10': 'zip'})
zip_merge = pd.merge(zip_demos, sewers_per_zip, on="zip", how = 'left') 

zip_merge.to_csv("zip_merge.csv")

fig, ax = plt.subplots()

#sns.lmplot(x ='sewer_density', y = 'Median_Income', data = zip_merge)
sea = plt.show()
fig.savefig(f"scatter.png")



ax.set_ylabel('Land-Use Category')
ax.set_xlabel('% of Documented Parcel Sewage Connections')

plt.show()
fig.tight_layout()
fig.savefig(f"sewer share raw # by land-use.png")

heatmap_data = pd.read_csv('zip_inc_sew_density.csv')
heatmap_data['median_income'] = heatmap_data['median_income']/10000


#heatmap of sewage connections density per zip code vs median income


pivot_df = heatmap_data.pivot_table(values='median_income', index='zip', columns='density')

fig, ax = plt.subplots()

sns.set(font_scale=0.7)
sns.heatmap(pivot_df,annot=True, cmap='Spectral')
ax.set_title("Median Income vs Density of Sewer Connections per Land Area")


ax.set_xlabel("Sewer Density per Zip Code")
ax.set_ylabel("Median Income")

fig.tight_layout()
fig.savefig('heatmap.png')


#heatmap of WWTps density per zip code vs median income

heatmap_data2 = pd.read_csv('wwtp_zip_demos_heat.csv')
heatmap_data2['median_income'] = heatmap_data2['median_income']/10000


pivot_df = heatmap_data2.pivot_table(values='median_income', index='zip', columns='density')

fig, ax = plt.subplots()

sns.set(font_scale=0.7)
sns.heatmap(pivot_df,annot=True, cmap='Spectral')
ax.set_title("Median Income vs Geographic Density of WWTPs")


ax.set_xlabel("WWTP Density per Zip Code")
ax.set_ylabel("Zip Code's Median Income")

fig.tight_layout()
fig.savefig('heatmap2.png')





