
### FROM here , we can get the avergae temperature , Relative Humidity and Rainfall using the
### Coordinates of a point.

import requests
from datetime import datetime, timedelta
import numpy as np

def get_weather_info(lat, lon):

    try : 

        
        year = 2019,2020,2021,2022,2023,2024
        TEMP = []
        RH = []
        RAIN = []
        for i in year:
            url = (
                "https://power.larc.nasa.gov/api/temporal/daily/point"
                "?parameters=T2M,RH2M,PRECTOTCORR"
                f"&community=AG&latitude={lat}&longitude={lon}"
                f"&start={year}0101&end={year}1231&format=JSON"
            )
    
            response = requests.get(url)
            data = response.json()
            Temperature_List = list(data['properties']['parameter']['T2M'].values())
            RH_list = list(data['properties']['parameter']["RH2M"].values())
            Rain_list = list(data['properties']['parameter']['PRECTOTCORR'].values())

            TEMP.append(Temperature_List)
            RH.append(RH_list)
            RAIN.append(Rain_list)

        #Made by Kunsh Bhatia 
        return {
            "Average Temperature" : round(sum(TEMP)/len(TEMP) , 2 ),
            "Average Relative Humidity" : round(sum(RH)/len(RH),2),
            "Average Rain" : round((sum(RAIN)/60), 2) 
        }
    
    except:
        print("Unable to get information for the specific point marked\nMake Sure to Enter the value such that:Latitude :- [-90,90] AND Longitude :- [-180,180]")

#Made by Kunsh Bhatia 
