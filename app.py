import streamlit as st
from utils.model import get_valid_catoricals
import pandas as pd

def main():
    st.title("Enter Kickstarter Project Details")

    available_categories, available_subcategories, available_countries = get_valid_catoricals()

    # User input fields
    name = st.text_input("Enter a name:")
    category = st.selectbox("Select a Category:", available_categories, index=0)
    subcategory = st.selectbox("Select a Sub-Category:", available_subcategories, index=0)
    country = st.selectbox("Select a Country:", available_countries, index=0)
    launch_date = st.date_input("Enter Launch Date:")
    deadline_date = st.date_input("Enter Deadline Date:")
    goal = st.number_input("Enter Project Goal in $:", value=0, step=1)

    # Display the result
    if st.button("Show Result"):
        st.success(f"Name: {name}, Category: {category}, Sub-Category: {subcategory}, Country: {country}, Launch Date: {launch_date}, Deadline: {deadline_date}, Goal: {goal} ")

if __name__ == "__main__":
    main()