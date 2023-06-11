## 다중선형회귀분석을 이용한 예측 문제 해결

import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv")

## 데이터 전처리
df = df.dropna(axis=0)
#ocean_proximity는 범주형 값으로 분석에서 제외
df = df.drop("ocean_proximity", axis=1)

## 분석 데이터셋 준비
X = df.drop("median_house_value", axis=1)
y = df['median_house_value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

## 데이터분석 수행
lr = LinearRegression()
lr.fit(X_train, y_train)

print("기울기: ", lr.coef_)
print("y절편: ", lr.intercept_)

pred = lr.predict(X_test)

##성능평가 및 시각화
from sklearn.metrics import r2_score
score = r2_score(y_test, pred)
print(score)

pred1 = lr.predict(X_train)
score1 = r2_score(y_train, pred1)
print(score1)