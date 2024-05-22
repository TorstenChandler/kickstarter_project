from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, StandardScaler, RobustScaler, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

def drop_live(data:pd.DataFrame):
    return data[data.state != 'Live']

def duration(data:pd.DataFrame):
    data['launched'] = pd.to_datetime(data['launched'])
    data['deadline'] = pd.to_datetime(data['deadline'])
    data['duration'] = (data["deadline"] - data["launched"]).dt.days.astype(int)
    return data["duration"]

def split_date(data:pd.DataFrame):
    data['launched'] = pd.to_datetime(data['launched'])
    data['year'] = data["launched"].dt.year
    data['month'] = data["launched"].dt.month
    return data[['year','month']]

def scale(data:pd.DataFrame, scaler=None):
    if scaler == None:
        return data
    else:
        return scaler.fit_transform(data)

def create_preprocessor(scaler=None)->Pipeline:
    return Pipeline([
    ("drop", FunctionTransformer(drop_live)),
    ("ColumnTransformer", ColumnTransformer([
            ("duration", FunctionTransformer(duration), ["launched","deadline"]),
            ("split_date", FunctionTransformer(split_date), ["launched"]),
            ("scale", scale(scaler), ["goal", "backers"]),
            ("passthrough", FunctionTransformer(lambda data: data), ['category','subcategory', 'country'])
             
    ]))
])

KNN = Pipeline([
    ("pre_processing", create_preprocessor(scaler=RobustScaler())),
    ("KNN", KNeighborsClassifier())
])

random_forest = Pipeline([
    ("pre_processing", create_preprocessor()),
    ("random_forest", RandomForestClassifier())
    ]
)

__all__ = [logistical_regression,random_forest]