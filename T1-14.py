### city와 f4를 기준으로 f5의 평균값을 구한 다음, 
### f5를 기준으로 상위 7개 값을 모두 더해 출력하시오 (소수점 둘째자리까지 출력)

import numpy as np
import pandas as pd

dt = pd.read_csv("basic1.csv")
f5_mean = dt.groupby(['city', 'f4'])['f5'].mean()
df = f5_mean.to_frame()
df = df.sort_values('f5', ascending=False)
df_sum = df['f5'][0:7].sum()

print(round(df_sum,2))
