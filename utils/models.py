from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
import pandas as pd
def success(data: pd.DataFrame):
    data.success = 1 if data.pledge >= data.goal else 0
    
    return data['success']

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



pre_processing = Pipeline([
    ("drop", FunctionTransformer(drop_live)),
    ("ColumnTransformer", ColumnTransformer([
            ("success", FunctionTransformer(success), ["goal","pledged"]),
            ("duration", FunctionTransformer(duration), ["launched","deadline"]),
            ("split_date", FunctionTransformer(split_date), ["launched"])
    
             
    ], remainder='passthrough', remainder_cols=['category','subcategory', 'country', 'backers', 'goal']))
])

KNN = Pipeline([
    (
        "pre_processing", pre_processing([])
       
    ),
    ("logreg", LogisticRegression())
    ]
)

random_forest = Pipeline([
    (
        "preprocess", 
        ColumnTransformer([
                        
        ])
    ),
    ("logreg", RandomForestClassifier())
    ]
)