# -*- coding: utf-8 -*-

import pandas as pd

fname = './data/iris.csv'
iris = pd.read_csv(fname)

print(iris)

print(iris.Species.value_counts())

print(iris.describe())














