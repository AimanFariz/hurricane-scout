import streamlit as st
import pandas as pd
import numpy as np
# import plotly.express as px
import time
from about import about_page
import os
from dotenv import load_dotenv
import requests
from io import BytesIO
# from compare import compare_page
# from home import home_page()

load_dotenv()
def home_page():
    st.title("Hurricane Scout")
    st.caption("Built with Streamlit | By: Aiman, CS + French @ The University of Tulsa '27")
    uploaded_files = st.file_uploader("Drop an external data file here (csv, xlsx)",accept_multiple_files=True)


    local_files = [
        r"C:\Users\user\OneDrive\Documents\Side Projects\Python\Streamlit\cumulative-transfer-app\naia njcaa\NAIA.csv",
        r"C:\Users\user\OneDrive\Documents\Side Projects\Python\Streamlit\cumulative-transfer-app\naia njcaa\NJCAA.csv"
    ]
    # ncaa_d1_file_id = os.getenv("NCAA_D1_F24_ID")
    ncaa_d1_file_id = st.secrets["NCAA_D1_F24_ID"]
    naia_file_id = st.secrets["NAIA_F24_ID"]
    njcaa_file_id = st.secrets["NJCAA_F24_ID"]
    # ncaa_d1_file_id = "1EbyMuNA_xJvtpHKYEOBTFhHTmw5nE5b5"
    base_url = "https://drive.google.com/uc?id="
    ncaa_d1_url = f"{base_url}{ncaa_d1_file_id}"
    naia_url = f"{base_url}{naia_file_id}"
    njcaa_url = f"{base_url}{njcaa_file_id}"
    # Download the file
    response = requests.get(ncaa_d1_url)
    response.raise_for_status()  # Ensure the request was successful
    # Download the XLSX file
    # ncaa_d1_df = pd.read_excel(BytesIO(response.content), engine="openpyxl")
    ncaa_d1_df = pd.read_excel(ncaa_d1_url)
    naia_df = pd.read_excel(ncaa_d1_url)
    njcaa_df = pd.read_excel(ncaa_d1_url)
    
    st.header("NCAA D1 Fall 24 Dataframe")
    st.write(ncaa_d1_df)
    
    st.header("NAIA Fall 24 Dataframe")
    st.write(naia_df)
    
    st.header("NJCAA Fall 24 Dataframe")
    st.write(njcaa_df)
    # Process uploaded files if any
    if uploaded_files:
        files_to_process = uploaded_files
    else:
        files_to_process = local_files  # Fallback to local files
    for file in files_to_process:
        # Check if it's an uploaded file or a local file
        if isinstance(file, str):  # Local file (file path)
            filename = file.split("\\")[-1]  # Get the filename part
            name_part = filename.split(",")[0].split(".")[0]
            st.header(f"{name_part} Dataframe")
            dataframe = pd.read_csv(file) if file.endswith(".csv") else pd.read_excel(file)
        else:  # Uploaded file
            st.write(f"Processing uploaded file: {file.name}")
            if file.type == "text/csv":
                dataframe = pd.read_csv(file)
            else:
                dataframe = pd.read_excel(file)

        numeric_columns = dataframe.select_dtypes(include=['number']).columns.tolist()
        if numeric_columns:
            filter_conditions = []
            selected_columns = st.multiselect("Select Metrics", numeric_columns, default=numeric_columns[:min(3, len(numeric_columns))])
            for column in selected_columns:
                # Assuming column refers to a numeric column in the dataframe
                column_min = dataframe[column].min()
                column_max = dataframe[column].max()
                column_value = st.slider(
                    f"Set {column} value:", 
                    min_value=column_min, 
                    max_value=column_max, 
                    value=(column_min, column_max)  # Default value range
                )
                # Add filter condition for the current column
                filter_conditions.append((dataframe[column] >= column_value[0]) & (dataframe[column] <= column_value[1]))

            if selected_columns:
                if "Name" in dataframe.columns:
                    data = dataframe.set_index("Name")[selected_columns]
                else:
                    data = dataframe[selected_columns]
            # Apply the filter conditions
            if filter_conditions:
                filtered_data = dataframe[filter_conditions[0]]
                for condition in filter_conditions[1:]:
                    filtered_data = filtered_data[condition]
            else:
                filtered_data = dataframe
            # Display the dataframe
            # st.dataframe(data, use_container_width=True)
            st.dataframe(filtered_data, use_container_width=True)
        
