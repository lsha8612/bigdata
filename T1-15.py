### 주어진 데이터 셋에서 age컬럼 상위 20개의 데이터를 구한 다음 
### f1의 결측치를 중앙값으로 채운다.
### 그리고 f4가 ISFJ와 f5가 20 이상인 
### f1의 평균값을 출력하시오!

import numpy as np
import pandas as pd
dt = pd.read_csv("basic1.csv")

# age컬럼 상위 20개의 데이터 구하기
age_dt = dt['age'].sort_values(ascending=False).head(20)

# f1의 결측치를 중앙값으로 채운다
dt['f1'] = dt['f1'].fillna(dt['f1'].median())

# f4가 ISFJ와 f5가 20 이상인 f1의 평균값을 출력
print(dt[(dt['f4']=='ISFJ') & (dt['f5'] >= 20)]['f1'].mean())