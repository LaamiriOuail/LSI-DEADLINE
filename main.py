import streamlit as st
import pandas as pd
from datetime import datetime

def main():
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
                return ['background-color: gray'] * len(row)
            else:
                return [''] * len(row)
        except:
            return [''] * len(row)
    
    # Apply the highlight function to the dataframe
    styled_df = df.style.apply(highlight_dates, axis=1)
    # Convert datetime to date string
    #df['DATE'] = df['DATE'].dt.strftime('%d/%m/%Y')
    # Display the styled dataframe
    st.dataframe(styled_df)
if __name__=="__main__":
    main()