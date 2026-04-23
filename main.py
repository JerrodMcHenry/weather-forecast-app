import streamlit as st
import plotly.express as px
from backend import get_data
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = BASE_DIR / "images"


# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forcasted days")
option = st.selectbox("Select data to view", ("Temperature",
                                               "Sky"))
st.subheader(f"{option} in {place} for the next {days} days")

if place:
#Get the temperature/sky data
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        #Create a temperature plot
        figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": str(IMAGES_DIR/"clear.png"), "Clouds": str(IMAGES_DIR/"cloud.png"), "Rain": str(IMAGES_DIR/"rain.png"), "Snow": str(IMAGES_DIR/"snow.png")}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        
        image_paths = []
        for condition in sky_conditions:
            path = images.get(condition)
            if path:
                image_paths.append(str(path))
            else:
                st.write(f"No image mapped for: {condition}")

        if image_paths:
            st.image(image_paths, width=100)