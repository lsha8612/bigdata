###1번. airquality 데이터에 대해서 결측치가 가장 많은 변수를 찾아서 해당 결측치를 0으로 대치하고,
###     결측치를 제외한 평균과 0으로 대치한 후의 평균과의 차이를 구하시오.
import pandas as pd

dt = pd.read_csv('airquality.csv')

##결측치가 가장 많은 변수는 Ozone으로, 결측치 총 37개
print(dt['Ozone'].isnull().sum())
##대체 전 평균
Ozone_mean = dt['Ozone'].mean()
print(Ozone_mean)

##결측치를 0으로 대체
dt['Ozone'].fillna(0, inplace=True)
##대체 후 결측치 개수 확인
print(dt['Ozone'].isnull().sum())
##대체 후 평균
Ozone_mean1 = dt['Ozone'].mean()
print(Ozone_mean1)

##두 평균의 차이
print('두 평균값의 차이는: ', Ozone_mean-Ozone_mean1)

###2번. Wind 변수에 대해서 Min-Max 정규화를 수행한 후 평균값과
###     Z 정규화를 수행한 후 평균값의 차이를 구하시오.

#Min-Max 정규화
import numpy as np
Min = np.min(dt['Wind'])
Max = np.max(dt['Wind'])
dt['min_max'] = round((dt['Wind']-Min)/(Max-Min), 2)

##Z 정규화
Mean = np.mean(dt['Wind'])
Std = np.std(dt['Wind'])
dt['Z'] = round((dt['Wind']-Mean)/Std, 2)

m1= dt['min_max'].mean()
m2= dt['Z'].mean()
print('정규화 후 평균갑 차이: ',m1-m2 )

###3번. 월별(5월~9월) 평균 기온을 구하시오.
print(dt.groupby('Month')['Temp'].mean())