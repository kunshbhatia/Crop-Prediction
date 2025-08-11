### Parameters :- Temperature, Humidity, Rainfall, Nitrogen, Phosphorus, Potassium and pH

from application import final_model
from Crop_Data_Prediction.model_pred import model_func
import streamlit as st
import pandas as pd
import random
from streamlit_folium import st_folium
import folium
import requests
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(
    page_title="Crop Prediction",
    page_icon="🌱",
    layout="wide", 
)

st.markdown("<h2 style='text-align: center;'> 🌱 Find Best Crop For Sowing Purposes 🌰 </h2>"
            , unsafe_allow_html=True)

method = st.radio("Choose how you want to provide location:", 
                  ["Manually Type The Coordinates ✏️","Mark The Location On The Map 🗺️"])

lat,lon = 34,46  # Default parameters

if method == "Manually Type The Coordinates ✏️":
    with st.expander("Manually Type The Coordinates ✏️", expanded=True):
        lat = st.number_input("Latitude", min_value=-90.0, max_value=90.0, format="%.2f", value=32.3)
        lon = st.number_input("Longitude", min_value=-180.0, max_value=180.0, format="%.2f", value=43.5)

elif method == "Mark The Location On The Map 🗺️":
    with st.expander("Mark The Location On The Map 🗺️", expanded=True):
        col1, col2 = st.columns([1, 2])
        with col2:
            map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
            map.add_child(folium.LatLngPopup())
            map_data = st_folium(map, width=700, height=500)

        with col1:
            st.subheader("📌 Select The Coordinates")
            st.markdown("1) Zoom In or Out to get to the desired location on the map\n2) Press the area whose information is needed\n3) Click the submit button below.")
            if map_data and map_data["last_clicked"]:
                lat = map_data["last_clicked"]["lat"]
                lon = map_data["last_clicked"]["lng"]
                st.success(f"Latitude: {lat:.5f}")
                st.success(f"Longitude: {lon:.5f}")
            else:
                st.info("Click on the map to get coordinates.")


# Form
with st.form("Crop Predict"):          
    submitted = st.form_submit_button("Submit")

    if submitted:
        try:
            facts = [
                    "One teaspoon of healthy soil contains over a billion microorganisms. 🦠","Soil stores three times more carbon than the atmosphere. 🌍","Red soil indicates high iron oxide content. 🧱","Rain can carry pollutants and dust from the atmosphere to the ground. 🌧️","It takes around 500 years to form one inch of topsoil. ⏳","Lightning helps convert atmospheric nitrogen into usable forms for plants. ⚡","Clay soil holds water and nutrients better than sandy soil. 🪨","Virga is rain that evaporates before reaching the ground. 🌫️","Extreme weather events are increasing due to climate change. 🌪️","Wind and rain erosion can remove valuable topsoil. 💨","Soil pH affects nutrient availability to plants. 🧪","Healthy soil can retain more water and reduce the risk of drought. 💧","Dark soil usually contains more organic matter. 🌑","Sandy soil drains quickly but holds fewer nutrients. 🏜️","Soil temperature affects seed germination and root growth. 🌡️","Frozen soil can crack pipes and damage plant roots. ❄️","Photosynthesis depends on weather factors like sunlight and temperature. ☀️","Drought can lead to soil compaction and reduced fertility. 🌵","Flooding can wash away topsoil and leach nutrients. 🌊","Organic farming improves soil structure and biodiversity. 🌱"
                    ]
            
            with st.spinner(f'Loading . Do your know that :- {random.choice(facts)}'):
                Temperature, RH, Rain, N, Ph, Phosphorus, Potassium = final_model(lat, lon)
                Pred_Crop = model_func(Temperature,RH,Ph,Rain)
            def info_card(title, value, icon, unit=""):
                st.markdown(f"""
                <div style="background-color: #f0f2f6; padding: 20px; margin-bottom: 10px; margin-top: 5px; 
                        border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center;">
                    <div style="font-size: 30px;">{icon}</div>
                    <div style="font-size: 18px; font-weight: bold; margin-top: 5px;">{title}</div>
                    <div style="font-size: 24px; color: #0072C6;">{value} {unit}</div>
                </div>
                """, unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)
            with col1:
                info_card("Temperature", Temperature, "🌡️", "°C")
            with col2:
                info_card("Humidity", RH, "💧", "%")
            with col3:
                info_card("Rainfall", Rain*10, "🌧️", "mm") # Done to get the data back to original value earlier was scaled to 0.1

            col4, col5, col6, col7 = st.columns(4)
            with col4:
                info_card("Nitrogen", N, "🌱","	mg/kg")
            with col5:
                info_card("pH", Ph, "🧪")
            with col6:
                info_card("Phosphorus", Phosphorus, "🧬","mg/kg")
            with col7:
                info_card("Potassium", Potassium, "⚗️","mg/kg")
           
            st.markdown(f"""
            <div style="background-color: #e0f7da; padding: 30px; margin-top: 20px;
                    border-radius: 15px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
                <div style="font-size: 20px; font-weight: bold;">🌿 Based on Soil & Weather data, the best crop for sowing is:</div>
                <div style="font-size: 42px; font-weight: bold; color: #2e7d32; margin-top: 15px;">{Pred_Crop}</div>
            </div>
            """, unsafe_allow_html=True)
            #Made by Kunsh Bhatia 
            st.markdown("""
                <div style="background-color: rgba(255, 255, 255, 0.2); 
                    border: 1px solid #ccc; 
                    border-radius: 10px; 
                    padding: 15px; 
                    margin-top: 20px; 
                    text-align: center; 
                    font-size: 16px; 
                    color: #333;">
                    (The prediction is based on environmental factors and with the help of given dataset only NOT on the basis of location/altitude or type of land . For ground reality, please contact the respective departments of the area 😁)
                </div>
                """, unsafe_allow_html=True)

            st.write("")


            ### Common Q&A

            with st.expander("📄 Terms & Conditions"):
                st.markdown("""
                    By using this application, you agree that the soil and weather prediction results are based on publicly available soil and weather data.
                    The predictions are for educational and advisory purposes only and should not replace expert agricultural guidance.

                    - Data may vary slightly depending on external APIs.
                    - We do not store or share user location data.
                    - The best crop predicted by the model is based on limited dataset . Hence please refer a professional before taking any action in real conditions.
                """)

            with st.expander("📄 Which Dataset is used to train the model?"):
                st.markdown("""
                    You may find all the files of the dataset used to train the model below :-

                    - https://www.kaggle.com/datasets/kunshbhatia/crop-production-data-raw-refined
                    - Above dataset is with respect to Indian Crops and their relation with Climate and Weather.
                    """)
        
        # Main Error Block
        except:
            st.header("Some Error Occured , Please Try Again\nPossible Troubleshoot :-\n"
                        '1) Make sure that the marked location is not a river body or anything except the land.\n'
                        '2) Try clicking submit 3-4 times , sometimes server issue arises.\n'
                        '3) Check the coordinates entered.\n'
                        '4) The order with which coordinates are entered is correct i.e. latitude, then longitude.\n'
                        '5) Try using another set of coordinates.')
            
# Footer
st.markdown("""
    <hr style="margin-top: 2rem; margin-bottom: 0;">
    <div style="text-align: center; color: grey; font-size: 14px; padding: 10px 0;">
        © 2025 Kunsh Bhatia | Built with ❤️ and ☕
    </div>
""", unsafe_allow_html=True)

#Made by Kunsh Bhatia 
