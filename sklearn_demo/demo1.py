# -*- coding: utf-8 -*-
# @Time: 2022/8/18 10:27
# @Author: Min

# from sklearn import neighbors, datasets
#
# iris = datasets.load_iris()
# X, y = iris.data, iris.target
#
# # create the model
# knn = neighbors.KNeighborsClassifier(n_neighbors=5)
#
# # fit the model
# knn.fit(X, y)
#
# # What kind of iris has 3cm x 5cm sepal and 4cm x 2cm petal?
# # call the "predict" method:
# result = knn.predict([[3, 5, 4, 2],])
#
# print(iris.target_names[result])
import numpy as np
import unicodedata
import pandas as pd

def __IsNumber(input_data):
    result = False
    try:
        float(input_data)
        result = True
    except ValueError:
        pass

    if result:
        temp = float(input_data)
        if np.isnan(temp):
            return False
        if np.isinf(temp):
            return False

    if not result:
        try:
            import unicodedata
            unicodedata.numeric(input_data)
            result = True
        except (TypeError, ValueError):
            pass

    return result

flag = __IsNumber('四')
print(flag)