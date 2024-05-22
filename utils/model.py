from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import utils.constants as constants
import pandas as pd
__all__ = ["get_cleaned_data","split_datasplit_data","finetune_model"]

def get_cleaned_data(path):
    data = pd.read_csv("./data/kickstarter_projects.csv")
    data.columns = data.columns.str.lower()
    #@TODO: CREATE ADDITIONAL COLUMNS 
    return data

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

def finetune_model(model, params, xtrain, ytrain):
    """Performe hyperparameter tuning on your model

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

def get_valid_catoricals():
    df = get_cleaned_data("data/kickstarter_projects.csv")
    available_categories = df.category.to_list()
    available_subcategories = df.subcategory.to_list()
    available_countries = df.country.to_list()
    return available_categories, available_subcategories, available_countries
