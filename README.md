### Website Link : https://crop-prediction-application.streamlit.app/
# 🌾 Crop Prediction App

This project is a web-based application built with **Streamlit** that helps in predicting the most suitable crop for sowing based on current **environmental conditions** like soil parameters and weather data for the location provided by the **user**.

## 🚀 Features

- 📍 Interactive map to select your farming location based on your intrest  
- ✏️ Manual coordinate input for checking conditions of weather and which crop is best to grow abount the place
- 🌐 Auto-detect current location using IP 
- 📊 Real-time weather & soil data fetching using APIs  
- 🤖 Machine learning-based crop prediction ( Soul Purpose for the App 😁) 
- 🌱 Displays environmental parameters (Temperature, Humidity, Rainfall, pH, Nitrogen , Phosphorus and Potassium)  
- 📈 User-friendly for each and every parameter  
- 📋 Clear prediction summary  
- 📄 Educational facts and dataset information for transparency (Check below in the document for the link) 

## 📌 Technologies Used

- **Python**
- **Streamlit** (UI)
- **Scikit-learn** (ML model)
- **Folium / Streamlit-Folium** (Map integration)
- **Geopy / IPinfo API** (for location detection of the user)
- **OpenWeather, SoilGrids APIs** (to get environmental data)
- **Pandas, NumPy** for data handling , EDA etc.

## 🧠 ML Model

The model is trained using the [Crop Recommendation Dataset](https://www.kaggle.com/datasets/kunshbhatia/crop-production-data-raw-refined), and predicts the best crop based on:

- Temperature (°C)
- Humidity (%)
- Rainfall (mm)
- Soil pH (unitless)
- Nitrogen (mg/kg)
- Phosphorus (mg/kg)
- Potassium (mg/kg)

## 🗺️ How to Use

1. **Choose a method** to enter your location:
   - Type coordinates manually
   - Select from map ( My FAV 😋)
   - Auto-detect using IP
2. Click **Submit**
3. View the recommended crop based on soil & weather
4. Review other parameters and prediction summary

## 📝 Dataset Used

Crop Production Dataset from Kaggle:  
[🔗 https://www.kaggle.com/datasets/kunshbhatia/crop-production-data-raw-refined](https://www.kaggle.com/datasets/kunshbhatia/crop-production-data-raw-refined)

## ⚠️ Disclaimer

- Predictions are based on **environmental data only**
- Results are **based on dataset only**, please contact a substitute professional for agricultural before implimentation in real world
- Accuracy may vary based on data API quality


## 👨‍💻 Author

**Kunsh Bhatia**  
Built with ❤️ and ☕ using Streamlit  
Feel free to fork or contribute!
 # Crop-Prediction
