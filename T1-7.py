### 'f4'컬럼의 값이 'ESFJ'인 데이터를 'ISFJ'로 대체하고, 
### 'city'가 '경기'이면서 'f4'가 'ISFJ'인 데이터 중 'age'컬럼의 최대값을 출력하시오!

import pandas as pd
import numpy as np

dt = pd.read_csv("basic1.csv")

dt['f4'].replace('ESFJ', 'ISFJ')
print(dt[(dt['f4']=='ISFJ') & (dt['city']=='경기')]['age'].max())