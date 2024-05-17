from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer

"""
@TODO:
    1) CREATE NEW COLUMN FUNDED FROM (status) Live?
    2) NEW COLUMNS DURATION, MONTH, YEAR FROM START AND END
    3) SCALING UNCLEAR
"""

funded = FunctionTransformer(lambda row: True if row.pledged > row.goal else False)


logistical_regression = Pipeline([
    (
        "preprocess", 
        ColumnTransformer([
            
        ])
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

__all__ = [logistical_regression,random_forest]