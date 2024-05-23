import streamlit as st
import pandas as pd
import numpy as np 
import joblib
from utils.model import get_valid_catoricals, clean_data
model = joblib.load('./utils/pickles/ensemble.joblib')
def predict(project)->tuple:
    data = clean_data(pd.DataFrame(project))
    results = model.predict_proba(data)
    failure = results[0][0]
    success = results[0][1]
    return (failure,success)

def main():
    st.title("Enter Kickstarter Project Details")

    available_categories, available_subcategories, available_countries = get_valid_catoricals()

    # User input fields
    #user = st.selectbox("I am an :", ['Entrepreneur', 'Investor'], index=0)
    name = st.text_input("Enter Kickstarter Project Name:", value = "Awesome Project")
    goal = st.number_input("Enter Project Goal in $:", value=10000, step=1000)
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
    backers = st.number_input("Expected backers:", value=100)

    
    # Create a dictionary to store the input data
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

    # Convert the dictionary to a pandas DataFrame
    

    # Display the result
    if st.button("Predict Outcome"):
        failure, success = predict(data)
        if success >= 0.5:
            st.success(f"Project '{name}' has a {round(success*100)}% probability of Success!")
        else:
            st.error(f"Project '{name}' has a high probability of {round(failure*100)}% to fail. Consider revising the project or selecting another one.")
    #st.success(f"Name: {name}, Category: {category}, Sub-Category: {subcategory}, Country: {country}, Launch Date: {launch_date}, Deadline: {deadline_date}, Goal: {goal} ")

if __name__ == "__main__":
    main()

