import numpy as np
from sklearn.ensemble import RandomForestRegressor


def load_test_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        for _ in range(n):
            r, d = map(float, file.readline().strip().split('\t'))
            data.append((r, d))
    return n, data


def predict(model, test_data):
    X_test = np.array(test_data)
    predictions = model.predict(X_test)
    return predictions


def main():
    # print Radnom Forest Regression model loaded paramétricas
    params = {'bootstrap': True, 'ccp_alpha': 0.0, 'criterion': 'squared_error', 'max_depth': 10, 'max_features': 1.0, 'max_leaf_nodes': None, 'max_samples': None, 'min_impurity_decrease': 0.0,
              'min_samples_leaf': 2, 'min_samples_split': 5, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 100, 'n_jobs': None, 'oob_score': False, 'random_state': 42, 'verbose': 0, 'warm_start': False}
    model = RandomForestRegressor(**params)

    n, test_data = load_test_data('restaurants.in')
    predictions = predict(model, test_data)

    for prediction in predictions:
        print(prediction)


if __name__ == "__main__":
    main()
