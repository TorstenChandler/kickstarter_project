from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

logistical_regression = Pipeline([
    (
        "preprocess", 
        ColumnTransformer([
            
        ])
    ),
    ("logreg", LogisticRegression())
    ]
)