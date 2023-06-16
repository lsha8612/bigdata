### 모의고사 1회
### 2번. 은행에서 수집한 고객 5000명의 금융정보에 따른 대출여부가 들어있는 참조데이터를 이용하여
### 대출여부를 분류하는 가장 최적의 이웃의 크기값(k)을 구하고, 이때 분류정확도를 산출하시오.
### 단, 참조데이터는 7:3의 비율로 트레이닝 데이터와 테스트 데이터로 구분하고, 
### 트레이닝 데이터와 테스트 데이터의 대출여부(y)의 비율도 유지한다. 또한 normalizer 사용하여 스케일링 진행

import numpy as np
import pandas as pd

ploan = pd.read_csv('Bank_Personal_Loan_Modeling.csv')

## 의미 없는 변수와 결측값 제거
ploan_processed = ploan.dropna().drop(['ID', 'ZIP Code'], axis=1, inplace=False)
X = ploan_processed.drop(['Personal Loan'], axis=1)
y = ploan_processed['Personal Loan']

import sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234, stratify=y)

## normalizer 사용하여 스케일링 진행
from sklearn.preprocessing import Normalizer
preprocessor = Normalizer()
X_train = preprocessor.fit_transform(X_train)
X_test = preprocessor.fit_transform(X_test)

## 모델 생성
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

training_accuracy = []
test_accuracy = []
for n_neighbors in range(1,25):
    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    clf.fit(X_train, y_train)
    training_accuracy.append(clf.score(X_train, y_train))
    test_accuracy.append(clf.score(X_test, y_test))
    
for i in range(1, 25):
    print(i, '번째 정확도: ', test_accuracy[i-1])

## 최적의 k값은 5이고, 이 때 분류정확도는 92.6%이다.