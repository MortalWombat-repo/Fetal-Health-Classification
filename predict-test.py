#!/usr/bin/env python
# coding: utf-8

import requests
from colorama import Fore, Back, Style
import pandas as pd
import streamlit as st

url = "http://localhost:9696/predict"

# fetal health status
health_status = None

# Inital default values
fetus = {
        "baseline value": 120.0,
        "accelerations": 0.000,
        "fetal_movement": 0.000,
        "uterine_contractions": 0.000,
        "light_decelerations": 0.000,
        "severe_decelerations": 0.000,
        "prolongued_decelerations": 0.000,
        "abnormal_short_term_variability": 73.000,
        "mean_value_of_short_term_variability": 0.500,
        "percentage_of_time_with_abnormal_long_term_variability": 43.000,
        "mean_value_of_long_term_variability": 2.400,
        "histogram_width": 64.000,
        "histogram_min": 62.000,
        "histogram_max": 126.000,
        "histogram_number_of_peaks": 2.000,
        "histogram_number_of_zeroes": 0.000,
        "histogram_mode": 120.000,
        "histogram_mean": 137.000,
        "histogram_median": 121.000,
        "histogram_variance": 73.000,
        "histogram_tendency": 1.000
}

# """Streamlit"""
#st.image('img/image.png')
st.title('Fetal Health Classification')
st.sidebar.title("Health parameters")
st.sidebar.header("Use arrow buttons for maximum precision")
# Add a horizontal line (line break)
#st.sidebar.markdown("**____________________________________**")

st.sidebar.markdown("Baseline value")
# Slider with plus/minus buttons
baseline_value = st.sidebar.slider(
    label="Select a value between 106.0 and 160.0",  # Label for the slider
    min_value=106.0,  # Minimum allowed value
    max_value=160.0,  # Maximum allowed value
    value=120.0,      # Default value
    step=0.1,          # Step size for increments
    key="baseline_value"
)

# initialize the dictionary with the value
fetus["baseline value"] = baseline_value

st.sidebar.markdown("Accelerations")
# Slider with plus/minus buttons
accelerations = st.sidebar.slider(
    label="Select a value between 0.000 and 0.019",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=0.019,  # Maximum allowed value
    value=0.000,      # Default value
    step=0.001,
    key="accelerations"          # Step size for increments
)

# initialize the dictionary with the value
fetus["accelerations"] = accelerations

st.sidebar.markdown("Fetal movement")
# Slider with plus/minus buttons
fetal_movement = st.sidebar.slider(
    label="Select a value between 0.000 and 0.481",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=0.481,  # Maximum allowed value
    value=0.000,      # Default value
    step=0.001,
    key="fetal_movement"          # Step size for increments
)

# initialize the dictionary with the value
fetus["fetal_movement"] = fetal_movement

st.sidebar.markdown("Uterine contractions")
# Slider with plus/minus buttons
uterine_contractions = st.sidebar.slider(
    label="Select a value between 0.000 and 0.015",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=0.015,  # Maximum allowed value
    value=0.000,      # Default value
    step=0.001,
    key="uterine_contractions"                    # Step size for increments
)

# initialize the dictionary with the value
fetus["uterine_contractions"] = uterine_contractions

st.sidebar.markdown("Light decelerations")
# Slider with plus/minus buttons
light_decelerations = st.sidebar.slider(
    label="Select a value between 0.000 and 0.015",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=0.015,  # Maximum allowed value
    value=0.000,      # Default value
    step=0.001,
    key="light_decelerations"          # Step size for increments
)

# initialize the dictionary with the value
fetus["light_decelerations"] = light_decelerations

st.sidebar.markdown("Severe decelerations")
# Slider with plus/minus buttons
severe_decelerations = st.sidebar.slider(
    label="Select a value between 0.000 and 0.001",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=0.001,  # Maximum allowed value
    value=0.000,      # Default value
    step=0.001,
    key="severe_decelerations"          # Step size for increments
)

# initialize the dictionary with the value
fetus["severe_decelerations"] = severe_decelerations

st.sidebar.markdown("Prolongued decelerations")
# Slider with plus/minus buttons
prolongued_decelerations = st.sidebar.slider(
    label="Select a value between 0.000 and 0.005",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=0.005,  # Maximum allowed value
    value=0.000,      # Default value
    step=0.001,
    key="prolongued_decelerations"          # Step size for increments
)

# initialize the dictionary with the value
fetus["prolongued_decelerations"] = prolongued_decelerations

st.sidebar.markdown("Abnormal short term variability")
# Slider with plus/minus buttons
abnormal_short_term_variability = st.sidebar.slider(
    label="Select a value between 12.000 and 87.000",  # Label for the slider
    min_value=12.000,  # Minimum allowed value
    max_value=87.000,  # Maximum allowed value
    value=73.000,      # Default value
    step=0.001,
    key="abnormal_short_term_variability"          # Step size for increments
)

# initialize the dictionary with the value
fetus["abnormal_short_term_variability"] = abnormal_short_term_variability

st.sidebar.markdown("Mean value of short term variability")
# Slider with plus/minus buttons
mean_value_of_short_term_variability = st.sidebar.slider(
    label="Select a value between 0.200 and 7.000",  # Label for the slider
    min_value=0.200,  # Minimum allowed value
    max_value=7.000,  # Maximum allowed value
    value=0.500,      # Default value
    step=0.001,
    key="mean_value_of_short_term_variability"          # Step size for increments
)

# initialize the dictionary with the value
fetus["mean_value_of_short_term_variability"] = mean_value_of_short_term_variability

st.sidebar.markdown("Percentage of time with abnormal long term variability")
# Slider with plus/minus buttons
percentage_of_time_with_abnormal_long_term_variability = st.sidebar.slider(
    label="Select a value between 0.000 and 91.000",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=91.000,  # Maximum allowed value
    value=43.000,      # Default value
    step=0.001,
    key="percentage_of_time_with_abnormal_long_term_variability"          # Step size for increments
)

# initialize the dictionary with the value
fetus["percentage_of_time_with_abnormal_long_term_variability"] = percentage_of_time_with_abnormal_long_term_variability

st.sidebar.markdown("Mean value of long term variability")
# Slider with plus/minus buttons
mean_value_of_long_term_variability = st.sidebar.slider(
    label="Select a value between 0.000 and 50.700",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=50.700,  # Maximum allowed value
    value=2.400,      # Default value
    step=0.001,
    key="mean_value_of_long_term_variability"          # Step size for increments
)

# initialize the dictionary with the value
fetus["mean_value_of_long_term_variability"] = mean_value_of_long_term_variability

st.sidebar.markdown("Histogram width")
# Slider with plus/minus buttons
histogram_width = st.sidebar.slider(
    label="Select a value between 3.000 and 180.000",  # Label for the slider
    min_value=3.000,  # Minimum allowed value
    max_value=180.000,  # Maximum allowed value
    value=64.000,      # Default value
    step=0.001,
    key="histogram_width"          # Step size for increments
)

# initialize the dictionary with the value
fetus["histogram_width"] = histogram_width

st.sidebar.markdown("Histogram min")
# Slider with plus/minus buttons
histogram_min = st.sidebar.slider(
    label="Select a value between 50.000 and 159.000",  # Label for the slider
    min_value=50.000,  # Minimum allowed value
    max_value=159.000,  # Maximum allowed value
    value=62.000,      # Default value
    step=0.001,
    key="histogram_min"          # Step size for increments
)

# initialize the dictionary with the value
fetus["histogram_min"] = histogram_min

st.sidebar.markdown("Histogram max")
# Slider with plus/minus buttons
histogram_max = st.sidebar.slider(
    label="Select a value between 122.000 and 238.000",  # Label for the slider
    min_value=122.000,  # Minimum allowed value
    max_value=238.000,  # Maximum allowed value
    value=126.000,      # Default value
    step=0.001,
    key="histogram_max"          # Step size for increments
)

# initialize the dictionary with the value
fetus["histogram_max"] = histogram_max

st.sidebar.markdown("Histogram number of peaks")
# Slider with plus/minus buttons
histogram_number_of_peaks = st.sidebar.slider(
    label="Select a value between 0.000 and 18.000",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=18.000,  # Maximum allowed value
    value=2.000,      # Default value
    step=0.001,
    key="histogram_number_of_peaks"          # Step size for increments
)

# initialize the dictionary with the value
fetus["histogram_number_of_peaks"] = histogram_number_of_peaks

st.sidebar.markdown("Histogram number of zeroes")
# Slider with plus/minus buttons
histogram_number_of_zeroes = st.sidebar.slider(
    label="Select a value between 0.000 and 10.000",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=10.000,  # Maximum allowed value
    value=0.000,      # Default value
    step=0.001,
    key="histogram_number_of_zeroes"          # Step size for increments
)

# initialize the dictionary with the value
fetus["histogram_number_of_zeroes"] = histogram_number_of_zeroes

st.sidebar.markdown("Histogram mode")
# Slider with plus/minus buttons
histogram_mode = st.sidebar.slider(
    label="Select a value between 60.000 and 187.000",  # Label for the slider
    min_value=60.000,  # Minimum allowed value
    max_value=187.000,  # Maximum allowed value
    value=120.000,      # Default value
    step=0.001,
    key="histogram_mode"          # Step size for increments
)

# initialize the dictionary with the value
fetus["histogram_mode"] = histogram_mode

st.sidebar.markdown("Histogram mean")
# Slider with plus/minus buttons
histogram_mean = st.sidebar.slider(
    label="Select a value between 73.000 and 182.000",  # Label for the slider
    min_value=73.000,  # Minimum allowed value
    max_value=182.000,  # Maximum allowed value
    value=137.000,      # Default value
    step=0.001,
    key="histogram_mean"          # Step size for increments
)

# initialize the dictionary with the value
fetus["histogram_mean"] = histogram_mean

st.sidebar.markdown("Histogram median")
# Slider with plus/minus buttons
histogram_median = st.sidebar.slider(
    label="Select a value between 77.000 and 186.000",  # Label for the slider
    min_value=77.000,  # Minimum allowed value
    max_value=186.000,  # Maximum allowed value
    value=121.000,      # Default value
    step=0.001,
    key="histogram_median"          # Step size for increments
)

# initialize the dictionary with the value
fetus["histogram_median"] = histogram_median

st.sidebar.markdown("Histogram variance")
# Slider with plus/minus buttons
histogram_variance = st.sidebar.slider(
    label="Select a value between 0.000 and 269.000",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=269.000,  # Maximum allowed value
    value=73.000,      # Default value
    step=0.001,
    key="histogram_variance"          # Step size for increments
)

# initialize the dictionary with the value
fetus["histogram_variance"] = histogram_variance

st.sidebar.markdown("Histogram tendency")
# Slider with plus/minus buttons
histogram_tendency = st.sidebar.slider(
    label="Select a value between -1.000 and 1.000",  # Label for the slider
    min_value=-1.000,  # Minimum allowed value
    max_value=1.000,  # Maximum allowed value
    value=1.000,      # Default value
    step=0.001,
    key="histogram_tendency"          # Step size for increments
)

# initialize the dictionary with the value
fetus["histogram_tendency"] = histogram_tendency

# a trick for centering but it impacts the overall aesthetic as the title cant be centered without wrapping
#left_co, cent_co,last_co = st.columns(3)
#with cent_co:
#    st.image("img/image.png", caption="Sunrise by the mountains")
st.image("img/image.png")

#st.write("**Parameters chosen:**")
st.header(":gear: Parameters chosen: ")

# Convert dictionary to DataFrame
df = pd.DataFrame(fetus.items(), columns=["Feature", "Value"])

# Reset index does not work unfortunately, keeping this for future reference
df = df.reset_index(drop=True)

# Display as a dataframe (interactive and sortable) and hide the index
st.dataframe(df, use_container_width=True, hide_index=True)

# ""Streamlit Logic"""
if st.button("Predict Fetal Health"):
    response = requests.post(url, json=fetus).json()
    #print(response)
    #response["class"]
    fetal_health = response["class"]
    #print(fetal_health)
    match fetal_health:
        case 1:
            health_status = "Healthy"
            #print(f"The fetus health is rated to be {Back.GREEN}{health_status}{Style.RESET_ALL}")
            #print("The baby is healthy, no action needed.")
            #print("Healthy")
            st.write("")
            st.markdown(f"### The fetus health is rated to be :green[**{health_status}**] :smile:", unsafe_allow_html=True)
            st.markdown(f"#### The baby is healthy, no action needed.")
            #t.write("")
            st.image("img/fetus_green.png")
        case 2:
            health_status = "Suspect"
            #print(f"The fetus health is rated to be {Back.YELLOW}{health_status}{Style.RESET_ALL}")
            #print("The baby is suspected of having a medical problem, further monitoring advised.")
            #print("Suspect")
            st.write("")
            st.markdown(f"### The fetus health is rated to be :orange[**{health_status}**] :expressionless:", unsafe_allow_html=True)
            st.markdown(f"#### The baby is suspected of having a medical problem, further monitoring advised.")
            #st.write("")
            st.image("img/fetus_orange.png")
        case 3:
            health_status = "Pathological"
            #print(f"The fetus health is rated to be {Back.RED}{health_status}{Style.RESET_ALL}")
            #print("Immediate care is needed!")
            #print("Pathological")
            st.write("")
            st.markdown(f"### The fetus health is rated to be :red[**{health_status}**] :pensive:", unsafe_allow_html=True)
            st.markdown(f"#### Immediate care is needed!")
            #st.write("")
            st.image("img/fetus_red.png")


# """Terminal logic"""
response = requests.post(url, json=fetus).json()

fetal_health = response["class"]

match fetal_health:
    case 1:
        health_status = "Healthy"
        print(f"The fetus health is rated to be {health_status} 😊")
        print("The baby is healthy, no action needed.")
    case 2:
        health_status = "Suspect"
        print(f"The fetus health is rated to be {health_status} 😐")
        print("The baby is suspected of having a medical problem, further monitoring advised.")
    case 3:
        health_status = "Pathological"
        print(f"The fetus health is rated to be {health_status} 😔")
        print("Immediate care is needed!")
