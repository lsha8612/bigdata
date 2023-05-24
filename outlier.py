import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##이상치 처리 예제
##정규분포 50, 표준편차 10을 가지는 데이터 200개 생성 후 데이터프레임으로 변환
data = 10*np.random.randn(200) + 50
df = pd.DataFrame({'값':data})

##임의로 이상치 삽입
df.loc[201] = 2
df.loc[202] = 200
df.loc[203] = 10
df.loc[204] = 110

##분포 시각화
# plt.hist(df['값'], bins=20, rwidth=0.8)
# plt.show()

##boxplot 그림으로 이상치 확인
# plt.boxplot(df['값'])
# plt.show()

##사분위범위(quantile함수)
Q1 = df['값'].quantile(.25)
Q2 = df['값'].quantile(.5)
Q3 = df['값'].quantile(.75)
IQR = Q3-Q1 #사분위범위

# print("Q1 =", Q1)
# print("Q2 =", Q2)
# print("Q3 =", Q3)
# print("IQR =", IQR)

##이상치는 (3분위수+IQR*1.5)보다 큰 갑이거나, (1사분위수-IQR*1.5)보다 작은 값으로 검출된다.
condition = df['값'] > (Q3 + IQR * 1.5)
upper = df[condition]
condition = df['값'] < (Q1 - IQR * 1.5)
lower = df[condition]

# print(upper)
# print(lower)

##평활화 예제
dt1 = pd.read_csv('https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/datasets/lynx.csv')
print(dt1.head())
print(dt1.describe())

##10년 단순이동평균
dt1['sma'] = dt1['value'].rolling(10).mean()
# plt.plot(dt1['value'])
# plt.plot(dt1['sma'])
# plt.show()

##10년 지수가중이동평균
dt1['ewm'] = dt1['value'].ewm(10).mean()
plt.plot(dt1['value'])
plt.plot(dt1['ewm'])
plt.show()