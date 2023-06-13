###1번. airquality 데이터에 대해서 결측치가 가장 많은 변수를 찾아서 해당 결측치를 0으로 대치하고,
###     결측치를 제외한 평균과 0으로 대치한 후의 평균과의 차이를 구하시오.
import pandas as pd

df = pd.read_csv('airquality.csv')

##결측치가 가장 많은 변수는 Ozone으로, 결측치 총 37개
##대체 전 평균
Ozone_mean = df['Ozone'].mean()

##결측치를 0으로 대체
df['Ozone'].fillna(0, inplace=True)

##대체 후 평균
Ozone_mean1 = df['Ozone'].mean()

##두 평균의 차이
print(Ozone_mean  - Ozone_mean1)

###2번. Wind 변수에 대해서 Min-Max 정규화를 수행한 후 평균값과
###     Z 정규화를 수행한 후 평균값의 차이를 구하시오.

#Min-Max 정규화
import numpy as np
Min = np.min(df['Wind'])
Max = np.max(df['Wind'])
df['min_max'] = round((df['Wind']-Min)/(Max-Min), 2)
min_max_mean = df['min_max'].mean()

##Z 정규화
Mean = df['Wind'].mean()
Std = np.std(df['Wind'])
df['Z'] = round((df['Wind']-Mean)/Std, 2)
Z_mean = df['Z'].mean()

print(min_max_mean - Z_mean)

###3번. 월별(5월~9월) 평균 기온을 구하시오.
for i in range(5, 10):   
    temp = []
    print(i, "월 평균 기온: ", df[df['Month']==i]['Temp'].mean())
    
