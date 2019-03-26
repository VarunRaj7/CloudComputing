# P02_BigData_Analysis_Weather_data

This project is related to Data Analysis and processing using Apache Spark and/or HiveQL. The Project will use the weather dataset from https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/. This  project will use only 16 years of data ( 2000 - 2018)  for all the stations starting with US and elements TMAX, TMIN. 

The following information serves as a definition of each field in one line of data covering one station-day. 

Each field described below is separated by a comma ( , ) and follows the order presented in this document. 

ID = 11 character station identification code 

YEAR/MONTH/DAY = 8 character date in YYYYMMDD format (e.g. 19860529 = May 29, 1986) 

ELEMENT = 4 character indicator of element type  

DATA VALUE = 5 character data value for ELEMENT  

M-FLAG = 1 character Measurement Flag  

Q-FLAG = 1 character Quality Flag  

S-FLAG = 1 character Source Flag  

OBS-TIME = 4-character time of observation in hour-minute format (i.e. 0700 =7:00 am) 

See section III of the GHCN-Daily ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt  file for an explanation of ELEMENT codes and their units as well as the M-FLAG, Q-FLAGS and S-FLAGS. The OBS-TIME field is populated with the observation times contained in NOAA/NCDC’s Multinetwork Metadata System (MMS).   

Analysis Tasks: 

● Average TMIN, TMAX for each year excluding abnormalities or missing data 

● Maximum TMAX, Minimum TMIN for each year excluding abnormalities or missing data 

● 5 hottest , 5 coldest  weather stations for each year excluding abnormalities or missing data 

● Hottest and coldest day and corresponding weather stations in the entire dataset 

● Median TMIN, TMAX for each year and corresponding weather stations 

● Median TMIN, TMAX for the entire dataset  
