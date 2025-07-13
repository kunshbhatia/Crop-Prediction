from Programs.N_ph import fetch_soil
from Programs.Temp_RH_Rain import get_weather_info
import pandas as pd

lat = 67
lon = 28

data = fetch_soil(lat,lon)
data1 = get_weather_info(lat,lon)


if (data == str()):
    print("Error : " ,data)

elif (data1 == str()):
    print("Error : " ,data1)

else:
    Temperature = list(data1.values())[0]
    RH = list(data1.values())[1]
    Rain = list(data1.values())[2]
    N = list(data.values())[0]
    Ph = list(data.values())[1]
    
    marked_columns = ["Temperature" , "Relative Humidity" , "Precipitation" , "Nitrogen Content" , "Ph"]
    Columns = pd.DataFrame([[Temperature,RH,Rain,N,Ph]],columns=marked_columns)

    print(Columns)