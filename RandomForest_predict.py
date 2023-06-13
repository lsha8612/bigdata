## 랜덤포레스트를 이용한 예측 문제 해결

import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv("https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv")

df = df.dropna(axis=0)
df = df.drop('ocean_proximity', axis=1)

X = df.drop('median_house_value', axis=1)
y = df['median_house_value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

rtr = RandomForestRegressor(max_depth=3, random_state=42)
rtr.fit(X_train, y_train)

pred = rtr.predict(X_test)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, pred)
print(mse)