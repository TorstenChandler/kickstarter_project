from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

"""
@TODO:

    1) CREATE NEW COLUMN FUNDED FROM (status) Live?
    2) NEW COLUMNS DURATION, MONTH, YEAR FROM START AND END
    3) SCALING UNCLEAR
"""

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