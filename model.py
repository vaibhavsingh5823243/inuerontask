import pandas as pd
import numpy as np

import pickle
from pandas_profiling import ProfileReport
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
class Task:
    def __init__(self, data):
        self.data = pd.read_csv(data)

    def split_data(self):
        """This function will split the data
        into two part train and test."""
        try:
            data=self.data
            x = data.drop(columns=['UDI', 'Product ID', 'Type', 'Air temperature [K]'])
            y = data['Air temperature [K]']
            x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.75)
            return x_train, x_test, y_train, y_test
        except Exception as e:
            return e

    def model_creation(self):
         try:
            x_train, x_test, y_train, y_test = self.split_data()
            model = LinearRegression()
            model.fit(x_train, y_train)
            with open("model.pickle", "wb") as f:
                  pickle.dump(model, f)
            return True
         except Exception as e:
            return e

    def accuracy(self):
        try:
            x_train, x_test, y_train, y_test = self.split_data()
            model = pickle.load(open('model.pickle', 'rb'))
            accuracy = model.score(x_test, y_test)
            return accuracy
        except Exception as e:
            return e

    def predict(self, x):
        try:
            model = pickle.load(open('model.pickle', 'rb'))
            y_pred = model.predict(x)
            return y_pred
        except Exception as e:
            return e

    def test_case(self,number=10):
        try:
            x_train, x_test, y_train, y_test = self.split_data()
            x = np.array(x_test.iloc[:number])
            y_pred = self.predict(x)
            error = np.array(y_test[:number]) - y_pred
            test_result = {"Actual Value": np.array(y_test[:number]), "Predicted Value": y_pred, "Error": error}
            return test_result
        except Exception as e:
            return e

    def visualize(self):
        try:
            data=self.data
            data_v=ProfileReport(data)
            data_v.to_file('templates\\visualize.html')
            return True
        except Exception as e:
            return e
