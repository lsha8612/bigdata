import numpy as np
import pandas as pd
import sklearn
## 로지스틱 회귀 분류모델을 위한 패키지 임포트
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

## 데이터 전처리
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[['sepal_length']] = scaler.fit_transform(df[['sepal_length']])
df[['sepal_width']] = scaler.fit_transform(df[['sepal_width']])
df[['petal_length']] = scaler.fit_transform(df[['petal_length']])
df[['petal_width']] = scaler.fit_transform(df[['petal_width']])

## 분석 데이터셋 준비
X = df[['sepal_length','sepal_width','petal_length','petal_width']]
y = df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=11)

## 데이터 분석 수행
lr = LogisticRegression()
lr.fit(X_train, y_train)
pred = lr.predict(X_test)

## 정확도 평가
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, pred)
print(acc)
