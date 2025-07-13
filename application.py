from Programs.N_ph import fetch_soil
from Programs.Temp_RH_Rain import get_weather_info
import pandas as pd
from P_Prediction.P_prediction import P_prediction

lat = 28.7041 # "Please Enter the value such that:Latitude :- [-90,90] AND Longitude :- [-180,180]"
lon = 77.1025 # Enter this while making webiste

data = fetch_soil(lat,lon)
data1 = get_weather_info(lat,lon)

Temperature = list(data1.values())[0]
RH = list(data1.values())[1]
Rain = list(data1.values())[2]
N = list(data.values())[0]
Ph = list(data.values())[1]
Phosphorus = round(P_prediction(N,Temperature,RH,Ph,Rain)[0],2)

marked_columns = ["Temperature" , "Relative Humidity" , "Precipitation" , "Nitrogen Content" , "Ph" , "Phosphorus"]
Columns = pd.DataFrame([[Temperature,RH,Rain,N,Ph,Phosphorus]],columns=marked_columns)

print(Columns)