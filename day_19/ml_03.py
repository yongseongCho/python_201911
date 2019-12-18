# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

X = pd.DataFrame(iris.data)
X.columns = iris.feature_names
print(X)

y = pd.Series(iris.target)
print(y)

print(y.value_counts())

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()
model.fit(X, y)
print(model.score(X, y))












