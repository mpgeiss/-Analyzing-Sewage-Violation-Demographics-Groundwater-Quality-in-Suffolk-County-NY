# -Analyzing-Sewage-Violation-Demographics-Groundwater-Quality-in-Suffolk-County-NY

##  Summary and Motivating Question: 
Long Island faces unique water quality concerns because most buildings use onsite wastewater treatment systems (OWTS), which include septic tanks and leach fields, that directly discharge contaminants from filtered water into the only drinking water aquifer that more than 3 million Long Island residents drink from. 

This analysis specifically looked at parcel-level data about wastewater processing infrastructure to assess which properties send their sewage to a central treatment plant and which have septic systems and directly Dump effluent into nearby groundwater. The goal is to analyze how the density of properties that have sewage connection infrastructure varies with geographic & demographic factors, including land-use, and zip-code level median income & total population.

##  Results: 
One drawback to this analysis is that Suffolk county has provided data about only approximately 23% of parcels in Suffolk County about if 	  they are connected to sewage systems or not. However, previous literature in the water quality in Field has identified that close to 75% of 	      county buildings lack sewage infrastructure.

State data about where wastewater treatment plants are located helps provide a picture that many urban areas lack a WWTP, including     	Huntingville. The data also indicates that coastal neighborhoods in the Hamptons have few waste water treatment facilities

For Properties without septic system connections, 31% are recreational condition, 30% are residential, and open spaces, 28% are vacant. By 	   ZIP Code, zip code 11968 (Southampton), 11901 (Riverhead), and 11978 (Westhampton Beach) have the most parcels with septic tanks. It is 	   surprising for Westhampton Beach, which has an airport, to not have more modern sewage infrastructure.
	
For tax parcels with sewer connections, 93% of them are located on residential properties for the data provided. 3% are located at 		commercial sites. For each ZIP Code, 11968, 11787, and 11946, respectively, have the highest number of parcels with sewer connections for 	  wastewater processing, which represent the Southampton region, smith town, & the Town of Hampton bays. ZIP Code 11767, part of Smithtown,           has the highest density of sewer connections per land area unit. Having a higher sooner density is likely favorable for surrounding drinking         water quality because it implies that fewer buildings are directly filtering & discharging wastewater onsite.
	


##  Input Data:
This analysis uses data from the 2018 American community service API, the Suffolk County Open Data Portal, the New York State GIS Portal, 	  and USGS Coram. Information about centroids for each tax parcel and wastewater facility locations were downloaded from the New York State           GIS Parcel information site.

Parcel data for New York State:
Available via New York State Parcel GIS Portal https://gis.ny.gov/parcels

Recent Sewage Activity Data: Describes Sewage Connections, Disconnections, & Permit activity 2012-2022
Available via Suffolk County Open Data Portal https://opendata.suffolkcountyny.gov/maps/residential-sewer-connection-and-discharge-permits/about.		
 
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

##  Figures:

Figure 1: Land-Use categories with white areas as residential for Suffolk County, LI, with data provided by Suffolk County Open Data Portal
Shows: 
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

Figure 5: Plotting parcels with sewage locations (yellow) with land-use for each parcel

![sewage locations by land use](https://user-images.githubusercontent.com/65619679/236971258-61272a2e-7aa2-4eab-bbce-a6f31ad46766.png)
<img width="609" alt="Screen Shot 2023-05-08 at 9 29 48 PM" src="https://user-images.githubusercontent.com/65619679/236971307-f871d68d-8360-4b25-ad40-b6427ca2660c.png">

Figure 6: Mapping  parcels with sewage locations (yellow) against WWTP locations (pink) atop land-use color file for Eastern County Suffolk Coast

![sewer connects zoom end island vs WWTPs](https://user-images.githubusercontent.com/65619679/236971773-7769af43-e551-463f-889d-4994b1eea7b4.png)

Figure 7: Median Pharmaceutical Concentrations (ng/L) for GW Sites within each ZIP Code atop parcel land-use layer

<img width="945" alt="image" src="https://user-images.githubusercontent.com/65619679/236975796-ed775d43-b546-42c1-9af3-18e45ab36f30.png">
<img width="609" alt="Screen Shot 2023-05-08 at 9 41 56 PM" src="https://user-images.githubusercontent.com/65619679/236972723-f9c348cd-8033-4822-b7b2-afa0a1d80ee8.png">

Figure 8: Median Pesticide Concentrations (ng/L) for GW Sites within each ZIP Code atop parcel land-use layer

<img width="958" alt="Screen Shot 2023-05-08 at 9 46 26 PM" src="https://user-images.githubusercontent.com/65619679/236973275-48a49da2-06fe-458a-8343-d5b30253515a.png">
<img width="476" alt="Screen Shot 2023-05-08 at 10 06 55 PM" src="https://user-images.githubusercontent.com/65619679/236975847-0e3c93ea-fc1c-4cc8-8647-1fe56040c777.png">

Figure 9: Number of WWTPs by Land Use
