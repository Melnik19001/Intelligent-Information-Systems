from sklearn.model_selection import train_test_split
import numpy as np

class Classifier:
    def __init__(self, dist_function=np.linalg.norm):
        self.__dist_function = dist_function

    def fit(self, X, y):
        self.__X_param = np.array(X)
        self.__y_param = np.array(y)
        self.__class_labels = list(set(y))
        return self

    def predict(self, X):
        X = np.array(X)

        # Stage 1
        dist_matrix = np.array([
            [
                self.__dist_function(xp - xt)
                for xp in self.__X_param
            ]
            for xt in X
        ])

        # Stage 2
        b_matrix = np.array([
            [
                dist_matrix[idx][self.__y_param == class_label].mean()
                for class_label in self.__class_labels
            ]
            for idx in range(len(X))
        ])

        return 1 + b_matrix.argmin(axis=1)
