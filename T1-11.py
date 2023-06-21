### min-max스케일링 기준 상하위 5% 구하기
### 주어진 데이터에서 'f5'컬럼을 min-max 스케일 변환한 후, 상위 5%와 하위 5% 값의 합을 구하시오

import numpy as np
import pandas as pd

df = pd.read_csv("basic1.csv")

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['f5'] = scaler.fit_transform(df[['f5']])

# 하위 5%, 상위 5% 값 구하기
lower = df['f5'].quantile(0.05)
upper = df['f5'].quantile(0.95)
print(lower+upper)
