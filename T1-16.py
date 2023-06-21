### 주어진 데이터 셋에서 f2가 0값인 데이터를 age를 기준으로 오름차순 정렬하고
### 앞에서 부터 20개의 데이터를 추출한 후 
### f1 결측치(최소값)를 채우기 전과 후의 분산 차이를 계산하시오 (소수점 둘째 자리까지)

import pandas as pd
import numpy as np

dt = pd.read_csv("basic1.csv")#
dt_0 = dt[dt['f2']==0]s
dt1 = dt_0.sort_values('age', ascending=True)
df = dt1.head(20)

# f1 결측치를 채우기 전, 분산
var1 =df['f1'].var()
print(var1)
# f1 결측치를 최소값으로 채운 후, 분산
df['f1'] = df['f1'].fillna(df['f1'].min())
var2 = df['f1'].var()

print(round(var1-var2, 2))