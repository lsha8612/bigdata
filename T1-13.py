# 상관관계 구하기
# 주어진 데이터에서 상관관계를 구하고, quality와의 상관관계가 가장 큰 값과, 가장 작은 값을 구한 다음 더하시오!
# 단, quality와 quality 상관관계 제외, 소수점 둘째 자리까지 출력

import numpy as np
import pandas as pd

dt = pd.read_csv("winequality-red.csv")

# 상관관계 구하기
dt_corr = dt.corr()

# quality와 quality 상관관계 제외
dt_corr = dt_corr[:-1]

# quality와의 상관관계가 가장 큰 값, 가장 작은 값
max_corr=abs(dt_corr['quality']).max()  #0.47
print(max_corr)
min_corr=abs(dt_corr['quality']).min()   #0.013
print(min_corr)
print(round(max_corr+min_corr, 2))
