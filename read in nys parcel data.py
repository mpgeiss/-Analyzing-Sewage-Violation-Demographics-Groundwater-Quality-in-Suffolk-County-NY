import fiona  #powerful reading package...Thank you to Professor Peter Wilcoxen for writing most of this script
import geopandas as gpd

#
#  Names of data files and CRS variable
#Note: you need to download the 2 zips directly below into the same folder with all other project data/info 1st.
#
county_file = 'tl_2020_us_county.zip'
centroids_file = 'NYS-Tax-Parcel-Centroid-Points.gdb.zip' #from NYS Parcel Centroid website, contains Parcel-level data for all NYS Counties!
WWTP_file = "Wastewater_Facility.zip"
#

#  Check contents of centroid database, get a few rows
#  to check field names, and get the CRS
#

print("layers in centroid file", fiona.listlayers(centroids_file) )
layer_name = 'NYS_Tax_Parcels_All_Centroid_Points'

check = gpd.read_file(centroids_file,layer=layer_name,rows=100)
print("use geopandas to check layer-names", check.columns )

crs = check.crs
print("default centroid crs:", crs )

#
#  Read the county file and pick out Suffolk to use as a mask
#  when reading the centroid file. 
#  Suffolk FIPS code = 103
#

print('Reading counties...',flush=True)
county = gpd.read_file(county_file)
suffolk = county.query( 'GEOID == "36103"' )
suffolk = suffolk.to_crs(crs)

#
#  Read the centroid file. The mask filters out centroids that
#  aren't in Suffolk, which reduces the load time substantially
#

print('Reading centroids...',flush=True)
raw = gpd.read_file(centroids_file,layer=layer_name,mask=suffolk)
trim = raw.query('COUNTY_NAME == "Suffolk"')

#
#  Save the result of Suffolk County Centroids to gpkg layer!
#

print('Saving selected centroids...',flush=True)
trim.to_file('suffolk.gpkg',layer='centroids')

#
#  Print sewer statistics
#

print( trim[['SEWER_TYPE','SEWER_DESC']].value_counts(dropna=False) )

print(trim[[ 'WATER_SUPPLY', 'WATER_DESC']].value_counts(dropna=False) )

#BAR: supply type, ... by prop value.  Flood map in.
#
