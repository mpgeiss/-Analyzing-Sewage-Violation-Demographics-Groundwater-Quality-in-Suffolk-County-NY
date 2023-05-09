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
![white areas blank residential](https://user-images.githubusercontent.com/65619679/236969691-8db621b2-a5a2-4440-bd1a-ce062048aa60.png)



