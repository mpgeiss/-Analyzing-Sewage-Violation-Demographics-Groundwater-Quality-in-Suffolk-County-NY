## Map-Construction How-To Guide in QGIS

This file provides an overview of a how to make the map shown in the figure panel of the ReadMe.md file displayed on the project repository homepage.

For figures one, two, three, five, seven, eight, all legends were taken from the layer styling tab in QGIS.

## Figure 1: 
For the first figure, which shows land-use information for each parcel in Suffolk County, I imported the 2016 land-use polygon shape file from the Suffolk County open data portal. To do so, I went under the layers tab, selected add layer, and then selected add vector layer. At that point, under the Source menu, my vector data set was the land-use zip file. For the desired colors by description, under the layers tab on the left side, I selected the paint brush-appearing Player styling tab and changed the symbol to categorized with ‘DESCRIPTIO’ as the value with a random color ramp.

## Figure 2:
To create a map showing known sewage connection locations and ZIP Codes color-coded by median income, I imported the US County ZIP Code zip file, the data set of new sewage connections provided by Suffolk County in a zip file, imported the state level parcel data about tax centroids, and the Suffolk Demographics Csv file created by the python script ‘generate census GW demographics by zip.py’ file. 

### 6 data preparation steps in QGIS

1: To filter the tax censured file two parcels with sewage connections for wastewater processing, first add the ‘ New York State tax parcels’ zip file as a vector layer. Under the layers tab, right click the centroid slayer and select the filter tab. Select the ‘SEWER_TYPE’ Field and set it equal to 2 or 3. Now the only centroids that are showing are parcels with known connections to central sewage systems.
2: To filter for properties with septic systems, filter the original tax centroid file to have ‘SEWER_TYPE’ = 1.
3: To filter the properties with recent sewage connection activity to connected sites, add the residential sewer connection zip file from Suffolk County. Under the filter tab, select the ‘ connected_ disconnected’ Fields and set it equal to the value ‘Connected’.
4: To produce the file of zip codes in Suffolk County, first, one needs to import the US county zip file. Under the filter option, one needs to select ‘State FP’ = 36 AND ‘CountyFP’ = ‘103’. The output is the boundary of Suffolk county.
5: For the ZIP Codes in Suffolk county, one needs to add the US ZIP Code zip file as a new vector layer. 
- To trim to the county, go under the Geo processing tab under the vector tab and select the clip option. 
- Then, the ZIP Code layer is the input, and Suffolk county is the overlay layer. The output is ZIP Codes in Suffolk.
6: Finally, to join ZIP Code demographic information to the ZIP Codes, import the ‘Suffolk county zip demographics csv file’ as a delimited text layer under the add layer tab in the layer drop-down.
- Next, right click the Suffolk County zip flyer under the layers menu on the left and select layer properties. Perform a join by selecting the green plus option on the bottom left. 
- Select all fields for the joined field, and use join_ for the custom name prefix. 
- Select the demographic information as the join layer, use associated ZIP Code layers for the join field and target field. The result will have census and groundwater quality information by ZIP Code joined to the each zip code region.

### Image production
For the zip code joined layer, I plotted the join_income category with the graduated layer style with a RdBu Color ramp with four classes for equal count Quantiles. Once you are satisfied with the map you are viewing, select the export map to image option under the project tab and change the resolution to 300 dpi.

## Figure 3:
For the third figure, the steps are exactly the same as the second one, except that for the joint ZIP Code layer, I plotted the join_population layer with five classes using equal quartiles and the ‘Cividis’ color ramp.

## Figure 4:
For the fourth figure, make sure that the wastewater treatment plant location points and the points showing properties with sewage connections are layered on top of the land-use later. Here, both the new sewage connection layer and the sewer locations from the tax centroid file are selected and colored yellow.

## Figure 5:
For the fifth figure, everything is the same as figure 4 except that the waste water treatment plant file is NOT selected.

## Figure 6: 
This figure is the exact same as figure 4. I just used the zoom feature to focus on the Southampton region before exporting the map to image.

## Figure 7:
Same format as figure 2 and 3. With sewage connections layers selected, adjusted the graduated style option for the ZIP Code layer. Here, the pharmaceutical layer is selected using a orange color ramp with natural breaks and 4 classes. Zoom in on Central Suffolk County to get this image.

## Figure 8: 
Same format as figure 2 and three, with sewage connections layers selected, adjusted the graduated style option for the ZIP Code layer. Here, the pesticide layer is selected using a orange color ramp with natural breaks and 4 classes. Zoom in on Central Suffolk County to get this image.

All other figures made in Python script 'analysis of counts by area.py'
