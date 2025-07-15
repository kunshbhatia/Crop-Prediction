from Programs.N_ph import fetch_soil
from Programs.Temp_RH_Rain import get_weather_info
import pandas as pd
from P_Prediction.P_prediction import P_prediction
from K_Prediction.K_prediction import K_prediction


def final_model(lat,lon):
# lat,lon = (28.6139,77.2090) # "Please Enter the value such that:Latitude :- [-90,90] AND Longitude :- [-180,180]"
# Enter this

    data = fetch_soil(lat,lon)
    data1 = get_weather_info(lat,lon)

    try:
        Temperature = list(data1.values())[0]
        RH = list(data1.values())[1]
        Rain = list(data1.values())[2]
        N = list(data.values())[0]
        Ph = list(data.values())[1]
        Phosphorus = round(P_prediction(N,Temperature,RH,Ph,Rain)[0],2)
        Potassium = round(K_prediction(N,Temperature,RH,Ph,Rain,Phosphorus)[0],2)

        return Temperature,RH,Rain,N,Ph,Phosphorus,Potassium
    
    except:
        raise Exception("Error Occured While Processing The Information")

    
#Made by Kunsh Bhatia 