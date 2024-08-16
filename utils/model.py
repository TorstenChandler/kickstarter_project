from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import utils.constants as constants
import pandas as pd
import numpy as np
__all__ = ["get_cleaned_data","split_datasplit_data","finetune_model"]

def clean_data(data:pd.DataFrame)->pd.DataFrame:
    data.columns = data.columns.str.lower()
    data['success'] =  data.apply(lambda row: 1 if row["pledged"] >= row["goal"] else 0, axis=1)
    return data

def get_cleaned_data(path):
    data = pd.read_csv(path)
    data = data[data.State != 'Live']
    return clean_data(data)

def extract_train(data):
    train, test = train_test_split(data, test_size=constants.TEST_SIZE, random_state=constants.RSEED)
    return train

def split_train_test(data, label):
    """split your data into x_train, x_test, y_train, y_test

    Args:
        data (DataFrame): your pandas dataframe
        label (string): define your target column

    Returns:
        
    """
    y = data[label]
    x = data.drop(label, axis=1)
    return train_test_split(x,y, test_size=constants.TEST_SIZE, random_state=constants.RSEED)

def finetune_models(models, xtrain, ytrain):
    best_fit = []
    for model, paramas in models:
        best_fit.append(finetune_model(model,paramas,xtrain,ytrain))
    return best_fit
    

def finetune_model(model, params, xtrain, ytrain):
    """Perform hyperparameter tuning on your model

    Args:
        model: _description_
        params: Dictionary of Hyperparameters and values for tuning
        train: Pandas DataFrame cotnaining your training data
        label: String specifying the target column of your training data

    Returns:
        _type_: _description_
    """ 
    model = GridSearchCV(model, params) 
    model.fit(xtrain, ytrain)
    return model


def get_valid_categoricals():
    df = get_cleaned_data("data/kickstarter_projects.csv")
    
    # Ensure the columns are referenced as strings
    available_categories = df['category'].unique().tolist()
    available_subcategories = df['subcategory'].unique().tolist()
    available_countries = df['country'].unique().tolist()
    
    return available_categories, available_subcategories, available_countries
    