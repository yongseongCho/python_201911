# -*- coding: utf-8 -*-

# 머신러닝에 사용할 데이터의 로딩
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)

print(X)
print(y)

# 앙상블 기법을 기반으로 분류작업을 수행할 수 있는
# RandomForestClassifier 클래스
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

model.fit(X, y)

print(model.score(X, y))

print(model.predict(X[-5:]))

print(y[-5:])













