### 주어진 데이터에서 2022년 5월 주말과 평일의 sales컬럼 평균값 차이를 구하시오 
### (소수점 둘째자리까지 출력, 반올림)

import numpy as np
import pandas as pd
df = pd.read_csv("basic2.csv")
df['Date'] =  pd.to_datetime(df['Date'])
condition = (df['Date'].dt.year==2022) & (df['Date'].dt.month==5) & ((df['Date'].dt.dayofweek == 5) | (df['Date'].dt.dayofweek == 6))
mean1 = df[condition]['Sales'].mean()
condition1 = (df['Date'].dt.year==2022) & (df['Date'].dt.month==5) & ((df['Date'].dt.dayofweek == 0) | (df['Date'].dt.dayofweek == 1) \
| (df['Date'].dt.dayofweek == 2)| (df['Date'].dt.dayofweek == 3)| (df['Date'].dt.dayofweek == 4))
mean2 = df[condition1]['Sales'].mean()
print(round(mean1-mean2, 2))