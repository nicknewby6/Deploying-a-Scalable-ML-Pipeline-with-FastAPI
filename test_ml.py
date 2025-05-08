import pytest
from sklearn.ensemble import RandomForestClassifier
from ml.model import (
    train_model,
    compute_model_metrics,
    inference)

# TODO: implement the first test. Change the function name and input as needed
def test_model_algortihm():
    """
    Ensure the model produces a RandomForestClassifier model.
    """
    X_train = [[1,1,1,1,1],[1,1,1,1,1]]
    y_train = [[1,1,1,1,1],[1,1,1,1,1]]
    m = train_model(X_train, y_train)
    assert isinstance(m, RandomForestClassifier) == True


# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Ensure the compute_model_metrics function returns the expected values.
    """
    y_test = [1,1,1,1]
    preds = [1,1,1,1]
    p, r, fb = compute_model_metrics(y_test, preds)
    metrics = [p, r, fb]
    assert metrics == [1, 1, 1]


# TODO: implement the third test. Change the function name and input as needed
def test_inference():
    """
    Ensure the inference function returns expected results.
    """
    X_train = [[1,1,1,1,1],[1,1,1,1,1]]
    y_train = [[1,1,1,1,1],[1,1,1,1,1]]
    X_test = [[1,1,1,1,1],[1,1,1,1,1]]
    rf = RandomForestClassifier()
    model = rf.fit(X_train, y_train)
    preds = inference(model, X_test)
    assert preds.all()==1
