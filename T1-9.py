### 주어진 데이터에서 'f5'컬럼을 표준화(Standardization (Z-score Normalization))하고 
### 그 중앙값을 구하시오

import pandas as pd
import numpy as np

df = pd.read_csv("basic1.csv")

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['f5'] = scaler.fit_transform(df[['f5']])
print(df['f5'].median())