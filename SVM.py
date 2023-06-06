import numpy as np
import pandas as pd
import sklearn
from sklearn import svm
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

##전처리 수행
d_mean = df['Age'].mean()
df['Age'].fillna(d_mean, inplace=True)
d_mode = df['Embarked'].mode()[0]
df['Embarked'].fillna(d_mode, inplace=True)
df['FamilySize'] = df['SibSp']+df['Parch']

##전처리 수행 - 원핫인코딩
onehot_sex = pd.get_dummies(df['Sex'])
df = pd.concat([df, onehot_sex], axis=1)
onehot_embarked = pd.get_dummies(df['Embarked'])
df = pd.concat([df, onehot_embarked], axis=1)

##분석 데이터셋 준비
X = df[['Pclass','Age','Fare','FamilySize','female','male','C','Q','S']]
y = df[['Survived']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

##데이터 분석 수행
sv = svm.SVC(kernel='rbf')
sv.fit(X_train, y_train)
pred = sv.predict(X_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, pred)
print(acc)

from sklearn.metrics import confusion_matrix
mat = confusion_matrix(y_test, pred)
print(mat)

from sklearn.metrics import classification_report
rpt = classification_report(y_test, pred)
print(rpt)