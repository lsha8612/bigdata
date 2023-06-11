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
X_train, X_test, y_train, y_test = 