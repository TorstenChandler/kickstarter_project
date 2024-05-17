from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

random_forest = Pipeline([
    (
        "preprocess", 
        ColumnTransformer([
            
        ])
    ),
    ("logreg", RandomForestClassifier())
    ]
)