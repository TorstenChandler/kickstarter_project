import streamlit as st
import pandas as pd
import numpy as np 
from utils.model import get_valid_catoricals

def predict(project : pd.DataFrame):
    return np.random.uniform(0, 1)

def main():
    st.title("Enter Kickstarter Project Details")

    available_categories, available_subcategories, available_countries = get_valid_catoricals()

    # User input fields
    user = st.selectbox("I am an :", ['Entrepreneur', 'Investor'], index=0)
    name = st.text_input("Enter Kickstarter Project Name:", value = "Awesome Project")
    country = st.selectbox("Select Project Country:", available_countries, index=0)

    # Create two columns for category and subcategory
    col_cat, col_subcat = st.columns(2)
    with col_cat:
        category = st.selectbox("Select Project Category:", available_categories, index=0)
    with col_subcat:
        subcategory = st.selectbox("Select Project Sub-Category:", available_subcategories, index=0)
    
    # Create two columns for launch_date and deadline_date
    col_launch, col_deadline = st.columns(2)
    with col_launch:
        launch_date = st.date_input("Enter Project Launch Date:")
    with col_deadline:
        deadline_date = st.date_input("Enter Project Deadline:")
    goal = st.number_input("Enter Project Goal in $:", value=10000, step=1000)

    # Create a dictionary to store the input data
    data = {
        "Project Name": [name],
        "Category": [category],
        "Sub-Category": [subcategory],
        "Country": [country],
        "Launch Date": [launch_date],
        "Deadline Date": [deadline_date],
        "Project Goal ($)": [goal]
    }

    # Convert the dictionary to a pandas DataFrame
    input = pd.DataFrame(data)

    # Display the result
    if st.button("Show Result"):
        result = predict(input)
        if result >= 0.5:
            st.success(f"Project '{name}' has a {round(result*100)}% probability of Success!")
        else:
            st.error(f"Project '{name}' is likely to be unsuccessful. Consider revising the project or selecting another one.")
    #st.success(f"Name: {name}, Category: {category}, Sub-Category: {subcategory}, Country: {country}, Launch Date: {launch_date}, Deadline: {deadline_date}, Goal: {goal} ")

if __name__ == "__main__":
    main()

