import streamlit as st
import pandas as pd
import numpy as np 
import joblib
from utils.model import get_valid_catoricals, clean_data
import datetime
model = joblib.load('./utils/pickles/xgboost.joblib')
def predict(project)->tuple:
    data = clean_data(pd.DataFrame(project))
    results = model.predict_proba(data)
    failure = results[0][0]
    success = results[0][1]
    return (failure,success)
available_categories, available_subcategories, available_countries = get_valid_catoricals()


st.title("Enter Kickstarter Project Details")
    
with st.form(key='kickstarter'):
    # User input fields
    #user = st.selectbox("I am an :", ['Entrepreneur', 'Investor'], index=0)
    name = st.text_input("Enter Kickstarter Project Name:", value = "Most Comfortable Insoles on Earth")
    goal = st.number_input("Enter Project Goal in $:", value=7500, step=100)
    country = st.selectbox("Select Project Country:", available_countries, index=0)

    # Create two columns for category and subcategory
    col_cat, col_subcat = st.columns(2)
    with col_cat:
        category = st.selectbox("Select Project Category:", available_categories, index=available_categories.index("Fashion"))
    with col_subcat:
        subcategory = st.selectbox("Select Project Sub-Category:",available_subcategories, index=available_subcategories.index("Footwear"))
    
    # Create two columns for launch_date and deadline_date
    col_launch, col_deadline = st.columns(2)
    with col_launch:
        launch_date = st.date_input("Enter Project Launch Date:",datetime.date(2024, 5, 15) )
    with col_deadline:
        deadline_date = st.date_input("Enter Project Deadline:", datetime.date(2024, 6, 6) )
    backers = st.number_input("Expected backers:", value=184)

    
    # Create a dictionary to store the input data
    

    # Convert the dictionary to a pandas DataFrame
    
    submit =st.form_submit_button("Predict Outcome")

    # Display the result
    if submit:
        data = {
            "Name": [name],
            "Category": [category],
            "Subcategory": [subcategory],
            "Country": [country],
            "Launched": [launch_date],
            "Deadline": [deadline_date],
            "Pledged": 0,
            "Goal": [goal],
            "Backers": backers
        }
        failure, success = predict(data)
        if success >= 0.5:
            st.success(f"Project '{name}' has a {round(success*100)}% probability of Success!")
        else:
            st.error(f"Project '{name}' has a high probability of {round(failure*100)}% to fail. Consider revising the project or selecting another one.")
    #st.success(f"Name: {name}, Category: {category}, Sub-Category: {subcategory}, Country: {country}, Launch Date: {launch_date}, Deadline: {deadline_date}, Goal: {goal} ")


