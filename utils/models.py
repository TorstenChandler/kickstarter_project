from sklearn.ensemble import RandomForestClassifier,VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, PolynomialFeatures,StandardScaler, RobustScaler, MinMaxScaler, OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import xgboost as xgb

def duration(data:pd.DataFrame):
    data['launched'] = pd.to_datetime(data['launched'])
    data['deadline'] = pd.to_datetime(data['deadline'])
    data['duration'] = (data["deadline"] - data["launched"]).dt.days.astype(int)
    return data[["duration"]]

def split_date(data:pd.DataFrame):
    data['launched'] = pd.to_datetime(data['launched'])
    data['year'] = data["launched"].dt.year
    data['month'] = data["launched"].dt.month
    return data[['year','month']]

def passthrough(data):
     return data

def scale(scaler):
        if scaler:
            return scaler
        else:
            return FunctionTransformer(passthrough)
        

def create_preprocessor(scaler=None)->Pipeline:
    return Pipeline([
    ("ColumnTransformer", ColumnTransformer([
            ("duration", FunctionTransformer(duration), ["launched","deadline"]),
            ("split_date", FunctionTransformer(split_date), ["launched"]),
            ("scale", scale(scaler), ["goal", "backers"]),
            ("passthrough", OneHotEncoder(drop="first"), ['category','subcategory', 'country'])
    ]))
])

knn = Pipeline([
    ("pre_processing", create_preprocessor(RobustScaler())),
    ("KNN", KNeighborsClassifier(n_jobs=-1, n_neighbors=3))

])

log_reg = Pipeline([
    ("pre_processing", create_preprocessor(RobustScaler())),
    ("log_reg", LogisticRegression(max_iter=1000, n_jobs=-1))

])

random_forest = Pipeline([
    ("pre_processing", create_preprocessor()),
    ("random_forest", RandomForestClassifier(n_jobs=-1, max_depth=5, max_leaf_nodes=20))
    ]
)

xgboost =  Pipeline([
     ("pre_processing", create_preprocessor()),
     ("xgb", xgb.XGBClassifier(objective='binary:logistic', n_estimators=100, learning_rate=0.1))
])


ensemble = VotingClassifier([
    ("log_reg", log_reg),
    ("random_forest", random_forest),
    ("knn", knn)
], voting="soft")