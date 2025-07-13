import pickle

def P_prediction(N,Temp,RH,Ph,Rainfall):

    with open("P_Prediction\P_pred_model.pkl","rb") as f:
        model = pickle.load(f)

    with open("P_Prediction\P_pred_scaler.pkl","rb") as f:
        scaler = pickle.load(f)


    Y_pred = model.predict(scaler.transform([[N,Temp,RH,Ph,Rainfall]]))
    return Y_pred