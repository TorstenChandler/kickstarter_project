from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

log_reg = Pipeline([
    (
        "preprocess", 
        ColumnTransformer([
            
        ])
    ),
    ("logreg", LogisticRegression())
    ]
)