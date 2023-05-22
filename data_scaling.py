import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##한국인, 일본인 각 성인 1000명 육류소비량 데이터 생성
korean = 5*np.random.randn(1000)+53.9 #평균은 53.9/표준편차는 5인 난수 1000개
japan = 4*np.random.randn(1000)+32.7 #평균은 32.7/표준편차는 4인 난수 1000개

df = pd.DataFrame({"한국인":korean, "일본인":japan})
#print(df)

##한국인 육류소비량 히스토그램
#plt.hist(korean)
#plt.xlabel('Korea')
#plt.show()

##중국인 육류소비량 히스토그램
#plt.hist(japan)
#plt.xlabel('Japan')
#plt.show()

##Z-표준화
import scipy.stats as ss

df['한국인 정규화'] = ss.zscore(korean)
df['일본인 정규화'] = ss.zscore(japan)

##직접 표준정규화식 입력
df['한국인 정규화1'] = (korean-np.mean(korean))/np.std(korean)
df['일본인 정규화1'] = (japan-np.mean(japan))/np.std(japan)


##사이킷런 스케일러를 이용한 정규화
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['한국인 정규화2'] = scaler.fit_transform(df[['한국인']])
df['일본인 정규화2'] = scaler.fit_transform(df[['일본인']])

#print(df.head())

##Min-Max 정규화
from sklearn.preprocessing import MinMaxScaler

df1 = pd.DataFrame({"한국인":korean, "일본인":japan})

scaler = MinMaxScaler()
df1['한국인_mm'] = scaler.fit_transform(df1[['한국인']])
df1['일본인_mm'] = scaler.fit_transform(df1[['일본인']])

##직접 식 입력하여 표준화
Min = np.min(korean)
Max = np.max(korean)
df1['한국인_m2'] = (df1[['한국인']]-Min) / (Max-Min)

Min = np.min(japan)
Max = np.max(japan)
df1['일본인_m2'] = (df1[['일본인']] - Min) / (Max-Min)

print(df1.head())