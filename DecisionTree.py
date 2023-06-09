## 의사결정나무를 이용한 분석 수행

import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv("https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv")

## 데이터 전처리
df = df.dropna(axis=0)
df = df.drop('ocean_proximity', axis=1)
corr = df.corr(method='pearson')

X = df.drop('median_house_value', axis=1)
y = df['median_house_value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

## DecisionTreeRegressor 객체 생성
dtr = DecisionTreeRegressor(max_depth=3, random_state=42)
dtr.fit(X_train, y_train)
pred = dtr.predict(X_test)

## 모델 성능 평가 - 테스트 데이터셋
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, pred)
print(mse)