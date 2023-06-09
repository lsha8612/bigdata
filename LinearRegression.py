import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/auto-mpg.csv")

## 데이터 전처리
df = df.dropna(axis=0)

## 분석 데이터셋 준비
X = df[['weight']]
y = df['mpg']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

## 데이터 분석 수행
lr = LinearRegression()
lr.fit(X_train, y_train)

## 회귀식의 기울기와 y절편
print("기울기: ", lr.coef_)
print("y절편: ", lr.intercept_)
pred = lr.predict(X_test)

## 정확도 측정
from sklearn.metrics import r2_score


