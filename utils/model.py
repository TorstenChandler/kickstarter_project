from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import utils.constants as constants

def split_data(data, label):
    """split your data into x_train, x_test, y_train, y_test

    Args:
        data (DataFrame): your pandas dataframe
        label (string): define your target column

    Returns:
        
    """
    y = data.pop(label)
    x = data
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

