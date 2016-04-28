# Flight-Delay-Prediction

##Team Members

1. Prateek Chandan (120050042)
2. Nishant Kumar Singh (120050043)
3. Maninder

## How to Run

To run the complete code base. Run the following bash file

   `./run.sh`
  
##Requirements
Language : **Python2.7**
Operating System : **Linux** 
Memory Requirement : *~40GB of free space*
The following python libraries are used in our code base and are required in this project

* pandas
* sklearn
* numpy
* scipy
* csv


##Data File Fileds
Note: The fileds with * are used in our training model
1.	*Year	1987-2008
2.	*Month	1-12
3.	DayofMonth	1-31
4.	*DayOfWeek	1 (Monday) - 7 (Sunday)
5.	*DepTime	actual departure time (local, hhmm)
6.	*CRSDepTime	scheduled departure time (local, hhmm)
7.	*ArrTime	actual arrival time (local, hhmm)
8.	*CRSArrTime	scheduled arrival time (local, hhmm)
9.	*UniqueCarrier	unique carrier code
10.	FlightNum	flight number
11.	TailNum	plane tail number
12.	*ActualElapsedTime	in minutes
13.	*CRSElapsedTime	in minutes
14.	*AirTime	in minutes
15.	->ArrDelay	arrival delay, in minutes
16.	->DepDelay	departure delay, in minutes
17.	*Origin	origin IATA airport code
18.	*Dest	destination IATA airport code
19.	*Distance	in miles
20.	TaxiIn	taxi in time, in minutes
21.	TaxiOut	taxi out time in minutes
22.	*Cancelled	was the flight cancelled?
23.	CancellationCode	reason for cancellation (A = carrier, B = weather, C = NAS, D = security)
24.	Diverted	1 = yes, 0 = no
25.	CarrierDelay	in minutes
26.	WeatherDelay	in minutes
27.	NASDelay	in minutes
28.	SecurityDelay	in minutes
29.	LateAircraftDelay	in minutes
30. source  Time
31. source  Station Type
32. source  Maintenance Indicator
33. source  Sky Conditions
34. *source  Visibility
35. source  Weather Type
36. *source  Dry Bulb Temp
37. *source  Dew Point Temp
38. *source  Wet Bulb Temp
39. *source  % Relative Humidity
40. *source  Wind Speed (kt)
41. source  Wind Direction
42. source  Wind Char. Gusts (kt)
43. source  Val for Wind Char.
44. *source  Station Pressure
45. source  Pressure Tendency
46. *source  Sea Level Pressure
47. source  Record Type
48. source  Precip. Total
49. dest  Time
50. dest  Station Type
51. dest  Maintenance Indicator
52. dest  Sky Conditions
53. *dest  Visibility
54. dest  Weather Type
55. *dest  Dry Bulb Temp
56. *dest  Dew Point Temp
57. *dest  Wet Bulb Temp
58. *dest  % Relative Humidity
59. *dest  Wind Speed (kt)
60. dest  Wind Direction
61. dest  Wind Char. Gusts (kt)
62. dest  Val for Wind Char.
63. *dest  Station Pressure
64. dest  Pressure Tendency
65. *dest  Sea Level Pressure
66. dest  Record Type
67. dest  Precip. Total

##Data Source

We have used the following data sets:

1. [**Statistical Computing & Statistical Graphics​** ](http://stat­computing.org/dataexpo/2009/the­data.html​) .This data is taken from the Research and Technology Administration (RITA) database and  structured for our use. But the above dataset doesn’t have any information related to weather conditions at the origin and destination airports.
2. For weather data we have: 
[**Hourly land­based weather observations from NOAA​**](http://cdo.ncdc.noaa.gov/qclcd_ascii/​) .This source contains hourly and daily data of weather at various airports.

## References
1. http://stat­computing.org/dataexpo/2009/the­data.html
2. http://cdo.ncdc.noaa.gov/qclcd_ascii/
3. https://www.scipy.org/
4. http://scikit-learn.org/
5. http://www.google.com
