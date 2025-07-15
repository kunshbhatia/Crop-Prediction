import pickle

def model_func(Temperature,RH,PH,Rain):

    with open("Crop_Data_Prediction/model_pred_model.pkl","rb") as f:
        model = pickle.load(f)

    with open("Crop_Data_Prediction/model_pred_scaler.pkl","rb") as f:
        scaler = pickle.load(f)

    with open("Crop_Data_Prediction/model_dict.pkl","rb") as f:
        list_ = pickle.load(f)

    Prediction = model.predict(scaler.transform([[Temperature,RH,PH,Rain]]))
    for crop,num in list_.items():
        if num == Prediction:
            Prediction_final = crop.upper()

    return Prediction_final
            
print(model_func(32,43,2.4,246))