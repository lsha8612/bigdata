import numpy as np
import pandas as pd
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

##텍스트로 되어 있는 species 컬럼의 데이터를 0, 1, 2로 변환
df['species'].replace({'setosa':0, 'versicolor':1, 'virginica':2}, inplace=True)

##학습용 데이터셋과 테스트용 데이터셋으로 구분
##X는 독립변수(설명변수), y는 종속변수(목표변수)
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=11)

##지도학습-분류 알고리즘 이용(의사결정나무 이용)
dt = DecisionTreeClassifier(random_state=11)
dt.fit(X_train, y_train)

##데이터셋으로 예측 수행
pred = dt.predict(X_test)

##모델 성능 - 정확도 측정
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, pred)
# print(acc)

##오차행렬 구하기
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, pred)

##모델 평가지표
from sklearn.metrics import classification_report
rpt = classification_report(y_test, pred)
print(rpt)