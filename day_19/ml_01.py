# -*- coding: utf-8 -*-

# 사이킷런 모듈
# - 머신러닝 알고리즘을 추상화하여(클래스로 구현한) 
# 구현해놓은 파이썬 라이브러리
# - conda install scikit-learn
import sklearn

# 머신러닝
# - 주어진 데이터를 학습하여, 
# 새로운 데이터를 통해 예측할 수 있는 방법
# - 지도학습 : 주어진 데이터가 정답이 존재하는 경우
# - 비지도학습 : 주어진 데이터가 정답이 없는 경우
# - 준지도학습 :주어진 데이터의 일부만 정답이 존재하는 경우
# - 강화학습 :주어진 데이터의 일부만 정답이 존재하는 경우

# 입력데이터 X
x = [[1],[2],[3],[4],[5]]

# 정답(라벨)데이터 y
y = [5,10,15,20,25]

# 선형회기 알고리즘을 구현하고 있는 LinearRegression 클래스
from sklearn.linear_model import LinearRegression

# 머신러닝 알고리즘을 구현하고 있는 클래스의 객체를 생성
model = LinearRegression()

# 학습
model.fit(x, y)

# 학습의 결과 테스트
print(model.score(x, y))

# 새로운 데이터를 적용하여 예측
print(model.predict([[10]]))































