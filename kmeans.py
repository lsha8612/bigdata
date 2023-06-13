import numpy as np
import pandas as pd
import sklearn
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

## 데이터 전처리
from sklearn.preprocessing import LabelEncoder
df['species'] = LabelEncoder().fit_transform(df['species'])
df_copy = df

## 변수간 상관관계 시각화
import seaborn as sns
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
# sns.pairplot(df, hue='species')
# plt.show()

## 데이터분석 수행
cluster1 = KMeans(n_clusters=3, n_init=10, max_iter=500, random_state=42, algorithm='auto')
cluster1.fit(df)
KMeans(max_iter=400, n_clusters=3, random_state=42)

cluster_center = cluster1.cluster_centers_
cluster_prediction = cluster1.predict(df)

df_copy['cluster'] = cluster_prediction

## 성능평가 및 시각화
scope =  range(1, 10)
inertias = []

for k in scope:
    model = KMeans(n_clusters=k)
    model.fit(df)
    inertias.append(model.inertia_)

plt.figure(figsize=(4,4))
plt.plot(scope, inertias, '-o')
plt.xlabel('number of cluster, k')
plt.ylabel('inertia')
plt.show()
