### 주어진 데이터 중 basic1.csv에서 'f4'컬럼 값이 
### 'ENFJ'와 'INFP'인 'f1'의 표준편차 차이를 절대값으로 구하시오

# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np
dt = pd.read_csv("basic1.csv")

# 조건에 맞는 데이터
enfj = dt[dt['f4']=='ENFJ']['f1'].std()
infp = dt[dt['f4']=='INFP']['f1'].std()

# 두 표준편차 차이를 절대값으로 구하시오
print(np.abs(enfj-infp))