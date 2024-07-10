from scipy.stats import mode
import numpy as np
import statistics as stats

from sklearn.base import RegressorMixin
from sklearn.base import ClassifierMixin
from collections import Counter

class MeanRegressor(RegressorMixin):
    # Predicts the mean of y_train

    def __init__(self, shift=0):
        self.shift = shift

    def fit(self, X=None, y=None):
        self.mean_ = np.mean(y) + self.shift
        return self

    def predict(self, X=None):
        M = 1 if X.ndim == 0 else X.shape[0]
        return np.full(M, self.mean_)
    

class MostFrequentClassifier(ClassifierMixin):
    # Predicts the most frequent class in y_train
    def fit(self, X=None, y=None):
        print(stats.mode(y))
        self.most_frequent_class_ = stats.mode(y)
        return self
    
    def predict(self, X=None):
        M = 1 if X.ndim == 0 else X.shape[0]
        return np.full(M, self.most_frequent_class_)
    