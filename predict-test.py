#!/usr/bin/env python
# coding: utf-8

import requests
from colorama import Fore, Back, Style
import streamlit as st

url = "http://localhost:9696/predict"

# fetal health status
health_status = None

fetus = {
        "baseline value": 120.0,
        "accelerations": 0.0,
        "fetal_movement": 0.0,
        "uterine_contractions": 0.0,
        "light_decelerations": 0.0,
        "severe_decelerations": 0.0,
        "prolongued_decelerations": 0.0,
        "abnormal_short_term_variability": 73.0,
        "mean_value_of_short_term_variability": 0.5,
        "percentage_of_time_with_abnormal_long_term_variability": 43.0,
        "mean_value_of_long_term_variability": 2.4,
        "histogram_width": 64.0,
        "histogram_min": 62.0,
        "histogram_max": 126.0,
        "histogram_number_of_peaks": 2.0,
        "histogram_number_of_zeroes": 0.0,
        "histogram_mode": 120.0,
        "histogram_mean": 137.0,
        "histogram_median": 121.0,
        "histogram_variance": 73.0,
        "histogram_tendency": 1.0
}


response = requests.post(url, json=fetus).json()
#print(response)
#response["class"]
fetal_health = response["class"]
#print(fetal_health)
match fetal_health:
    case 1:
        health_status = "Healthy"
        print(f"The fetus health is rated to be {Back.GREEN}{health_status}{Style.RESET_ALL}")
        print("The baby is healthy, no action needed.")
        #print("Healthy")
    case 2:
        health_status = "Suspect"
        print(f"The fetus health is rated to be {Back.YELLOW}{health_status}{Style.RESET_ALL}")
        print("The baby is suspected of having a medical problem, further monitoring advised.")
        #print("Suspect")
    case 3:
        health_status = "Pathological"
        print(f"The fetus health is rated to be {Back.RED}{health_status}{Style.RESET_ALL}")
        print("Immediate care is needed!")
        #print("Pathological")

"""Streamlit"""
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
    step=0.1          # Step size for increments
)

st.sidebar.markdown("Accelerations")
# Slider with plus/minus buttons
acceleration = st.sidebar.slider(
    label="Select a value between 0.000 and 0.019",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=0.019,  # Maximum allowed value
    value=0.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Fetal movement")
# Slider with plus/minus buttons
fetal_movement = st.sidebar.slider(
    label="Select a value between 0.000 and 0.481",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=0.481,  # Maximum allowed value
    value=0.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Uterine contractions")
# Slider with plus/minus buttons
uterine_contractions = st.sidebar.slider(
    label="Select a value between 0.000 and 0.015",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=0.015,  # Maximum allowed value
    value=0.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Light decelerations")
# Slider with plus/minus buttons
light_decelerations = st.sidebar.slider(
    label="Select a value between 0.000 and 0.015",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=0.015,  # Maximum allowed value
    value=0.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Severe decelerations")
# Slider with plus/minus buttons
severe_decelerations = st.sidebar.slider(
    label="Select a value between 0.000 and 0.001",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=0.001,  # Maximum allowed value
    value=0.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Prolongued decelerations")
# Slider with plus/minus buttons
prolongued_decelerations = st.sidebar.slider(
    label="Select a value between 0.000 and 0.005",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=0.005,  # Maximum allowed value
    value=0.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Abnormal short term variability")
# Slider with plus/minus buttons
abnormal_short_term_variability = st.sidebar.slider(
    label="Select a value between 12.000 and 87.000",  # Label for the slider
    min_value=12.000,  # Minimum allowed value
    max_value=87.000,  # Maximum allowed value
    value=73.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Mean value of short term variability")
# Slider with plus/minus buttons
mean_value_of_short_term_variability = st.sidebar.slider(
    label="Select a value between 0.200 and 7.000",  # Label for the slider
    min_value=0.200,  # Minimum allowed value
    max_value=7.000,  # Maximum allowed value
    value=0.500,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Percentage of time with abnormal long term variability")
# Slider with plus/minus buttons
percentage_of_time_with_abnormal_long_term_variability = st.sidebar.slider(
    label="Select a value between 0.000 and 91.000",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=91.000,  # Maximum allowed value
    value=43.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Mean value of long term variability")
# Slider with plus/minus buttons
mean_value_of_long_term_variability = st.sidebar.slider(
    label="Select a value between 0.000 and 50.700",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=50.700,  # Maximum allowed value
    value=2.400,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Histogram width")
# Slider with plus/minus buttons
histogram_width = st.sidebar.slider(
    label="Select a value between 3.000 and 180.000",  # Label for the slider
    min_value=3.000,  # Minimum allowed value
    max_value=180.000,  # Maximum allowed value
    value=64.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Histogram min")
# Slider with plus/minus buttons
histogram_min = st.sidebar.slider(
    label="Select a value between 50.000 and 159.000",  # Label for the slider
    min_value=50.000,  # Minimum allowed value
    max_value=159.000,  # Maximum allowed value
    value=62.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Histogram max")
# Slider with plus/minus buttons
histogram_max = st.sidebar.slider(
    label="Select a value between 122.000 and 238.000",  # Label for the slider
    min_value=122.000,  # Minimum allowed value
    max_value=238.000,  # Maximum allowed value
    value=126.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Histogram number of peaks")
# Slider with plus/minus buttons
histogram_number_of_peaks = st.sidebar.slider(
    label="Select a value between 0.000 and 18.000",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=18.000,  # Maximum allowed value
    value=2.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Histogram number of zeroes")
# Slider with plus/minus buttons
histogram_number_of_zeroes = st.sidebar.slider(
    label="Select a value between 0.000 and 10.000",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=10.000,  # Maximum allowed value
    value=0.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Histogram mode")
# Slider with plus/minus buttons
histogram_mode = st.sidebar.slider(
    label="Select a value between 60.000 and 187.000",  # Label for the slider
    min_value=60.000,  # Minimum allowed value
    max_value=187.000,  # Maximum allowed value
    value=120.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Histogram mean")
# Slider with plus/minus buttons
histogram_mean = st.sidebar.slider(
    label="Select a value between 73.000 and 182.000",  # Label for the slider
    min_value=73.000,  # Minimum allowed value
    max_value=182.000,  # Maximum allowed value
    value=137.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Histogram median")
# Slider with plus/minus buttons
histogram_median = st.sidebar.slider(
    label="Select a value between 77.000 and 186.000",  # Label for the slider
    min_value=77.000,  # Minimum allowed value
    max_value=186.000,  # Maximum allowed value
    value=121.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Histogram variance")
# Slider with plus/minus buttons
histogram_variance = st.sidebar.slider(
    label="Select a value between 0.000 and 269.000",  # Label for the slider
    min_value=0.000,  # Minimum allowed value
    max_value=269.000,  # Maximum allowed value
    value=73.000,      # Default value
    step=0.001          # Step size for increments
)

st.sidebar.markdown("Histogram tendency")
# Slider with plus/minus buttons
histogram_tendency = st.sidebar.slider(
    label="Select a value between -1.000 and 1.000",  # Label for the slider
    min_value=-1.000,  # Minimum allowed value
    max_value=1.000,  # Maximum allowed value
    value=1.000,      # Default value
    step=0.001          # Step size for increments
)


