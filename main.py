import streamlit as st
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

def main(file_path="data/deadelines.csv"):
    # Using Markdown and HTML for styling the title to be centered
    st.markdown("<h1 style='text-align: center;'>Projects/Exams Deadlines : </h1>", unsafe_allow_html=True)
    # Load the data and parse dates in the specified format
    df = pd.read_csv("data/deadelines.csv", dayfirst=True, parse_dates=['DATE'])
    # Get the current date
    current_date = datetime.now().date()
    
    # Function to highlight rows
    def highlight_dates(row):
        try:
            date_col = pd.to_datetime(row['DATE']).date()
            if date_col < current_date:
                return [''] * len(row)
            else:
                return [''] * len(row)
        except:
            return [''] * len(row)
    
    # Apply the highlight function to the dataframe
    styled_df = df.style.apply(highlight_dates, axis=1)
    # Convert datetime to date string
    df['DATE'] = df['DATE'].dt.strftime('%d/%m/%Y')
    # Display the styled dataframe
    st.dataframe(styled_df)

import requests


if __name__=="__main__":
    MODE = os.getenv("MODE")
    if MODE.lower() == "dev":
        main()
    elif MODE.lower() == "deployment":
        url = os.getenv("DATA_URL")
        response = requests.get(url)

        with open('deadelines.csv', 'wb') as f:
            f.write(response.content)
        main("deadelines.csv")