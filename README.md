# -Analyzing-Sewage-Violation-Demographics-Groundwater-Quality-in-Suffolk-County-NY

Summary and Motivating Question:
Long Island faces unique water quality concerns because most buildings use onsite wastewater treatment systems (OWTS), which include septic tanks and leach fields, that directly discharge contaminants from filtered water into the only drinking water aquifer that more than 3 million Long Island residents drink from. 

This analysis specifically looked at …

Results: 
	One drawback to this analysis is that Suffolk county has provided data about only approximately 23% of parcels in Suffolk County about if 	  they are connected to sewage systems or not. However, previous literature in the water quality in Field has identified that close to 75% of 	      county buildings lack sewage infrastructure.

	State data about where wastewater treatment plants are located helps provide a picture that many urban areas lack a WWTP, including     	Huntingville. The data also indicates that coastal neighborhoods in the Hamptons have few waste water treatment facilities

	WWTP count & Sewer count/land use

	Sewer count by income

	Sewer count per capita by ZIP (w/data)

Input Data:
	This analysis uses data from the 2018 American community service API, the Suffolk County Open Data Portal, the New York State GIS Portal, 	  and USGS Coram. Information about centroids for each tax parcel and wastewater facility locations were downloaded from the New York State           GIS Parcel information site.

	Parcel data for New York State:
	Available via New York State Parcel GIS Portal https://gis.ny.gov/parcels

	Recent Sewage Activity Data:
	Available via Suffolk County Open Data Portal https://opendata.suffolkcountyny.gov/maps/residential-sewer-connection-and-discharge-		permits/about
 
      New York State WWTP Locations Data:
      Available via NYS GIS Clearinghouse https://data.gis.ny.gov/search?categories=water

      Suffolk County Land Use Shapefile:
      Available via Suffolk County Open Data Portal https://opendata.suffolkcountyny.gov/search?tags=gis%20data
      
      USGS Groundwater data: Provided in 'sites.csv' file
     
Tableau: 
	The map is colored by median earnings per zip code, with red representing lower income & blue representing higher income

	The map contains the following for select property centroids:
	- Sewage Connection Status
	- Water Supply Type

	The map contains WWTPs

	The map contains the following for each ZIP Code:
	- Median income
	- Total Population
	- Number of WWTPs
	- Number of Buildings with Sewer Connections
	- Number of Buildings with no Sewer (OWTS)
	- Number of Buildings with Public Water Supply
	- Number of Buildings with Private Water Supply

Figures:

Figure 1: Land-Use categories with white areas as residential for Suffolk County, LI, with data provided by Suffolk County Open Data Portal

![white areas residential land uses](https://user-images.githubusercontent.com/65619679/236970174-9a7717b1-e668-4248-b638-78671fa7be4b.png)
<img width="609" alt="Screen Shot 2023-05-08 at 9 22 15 PM" src="https://user-images.githubusercontent.com/65619679/236970329-9e766f2c-8705-4ce3-b4f8-53d6cd996ff0.png">

Figure 2: Plotting parcels with sewage locations (yellow) against income by zip-code

![sewer locations given by income](https://user-images.githubusercontent.com/65619679/236970529-dbc8e2cc-037c-4884-9787-9f990d10e7c1.png)
<img width="443" alt="image" src="https://user-images.githubusercontent.com/65619679/236970569-c3d60155-609c-445e-9ef2-55bfb4fdba7a.png">

Figure 3: Plotting parcels with sewage locations (yellow) against total population by zip-code

![sewer locations by income share](https://user-images.githubusercontent.com/65619679/236970637-ad3f00bf-ce20-4cac-a65f-49ecdee118da.png)
<img width="368" alt="image" src="https://user-images.githubusercontent.com/65619679/236970607-67b5175f-c769-4ab8-ba08-fbc52484293c.png">

Figure 4: Plotting parcels with sewage locations (yellow) against WWTP locations (pink) atop land-use color file

![sewage connections vs  WWTP locations entire county](https://user-images.githubusercontent.com/65619679/236970742-6d52a89c-5d25-4fa9-b74f-610d02f8600e.png)





