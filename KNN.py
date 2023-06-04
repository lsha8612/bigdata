import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
##KNN분류모델을 위한 패키지 임포트
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

##데이터 전처리 - 4개의 독립변수에 대해 Min-Max정규화(모든 값을 0~1사이로)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[['sepal_length']] = scaler.fit_transform(df[['sepal_length']])
df[['sepal_width']] = scaler.fit_transform(df[['sepal_width']])
df[['petal_length']] = scaler.fit_transform(df[['petal_length']])
df[['petal_width']] = scaler.fit_transform(df[['petal_width']])

##분석 데이터셋 준비
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=11, test_size=0.2)

##데이터분석 수행 - KNN알고리즘 이용
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

##예측 수행
pred = knn.predict(X_test)

##정확도 평가
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, pred)
print(acc)

##모델 성능평가 - Confusion Matrix 계산
from sklearn.metrics import confusion_matrix
mat = confusion_matrix(y_test, pred)
print(mat)

##모델 성능평가 - 평가지표 계산
from sklearn.metrics import classification_report
rpt = classification_report(y_test, pred)
print(rpt)
