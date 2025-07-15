import pickle

def K_prediction(N,Temp,RH,Ph,Rainfall,P):

    with open("K_Prediction/K_pred_model.pkl","rb") as f:
        model = pickle.load(f)

    with open("K_Prediction/K_pred_scaler.pkl","rb") as f:
        scaler = pickle.load(f)


    Y_pred = model.predict(scaler.transform([[N,Temp,RH,Ph,Rainfall,P]]))
    return Y_pred

#Made by Kunsh Bhatia 