import numpy as np
import pandas as pd
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

##데이터 전처리 - 결측치 대체
age_mean = df['Age'].mean() #결측치를 평균으로 대체
df['Age'].fillna(age_mean, inplace=True)

embarked_mode = df['Embarked'].mode()[0] #결측치를 최빈값으로 대체
df['Embarked'].fillna(embarked_mode, inplace=True)

##데이터 전처리 - 레이블 인코딩
from sklearn.preprocessing import LabelEncoder
df['Sex'] = LabelEncoder().fit_transform(df['Sex'])
df['Embarked'] = LabelEncoder().fit_transform(df['Embarked'])

##데이터 전처리 - 파생변수 생성
df['FamilySize'] = df['SibSp'] + df['Parch']

##분석 데이터셋 준비
X = df[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'FamilySize']]
y = df['Survived']

##데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=11)

##분류 알고리즘-의사결정나무 이용
dt = DecisionTreeClassifier(random_state=11)
dt.fit(X_train, y_train)

##예측 수행
pred = dt.predict(X_test)

##정확도 측정
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, pred)
print(acc)

##의사결정나무 대신 KNN 이용
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
pred1 = knn.predict(X_test)
acc1 = accuracy_score(y_test, pred1)
print(acc1)
