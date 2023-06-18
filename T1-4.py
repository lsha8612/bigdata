### 주어진 데이터 중 train.csv에서 'SalePrice'컬럼의 왜도와 첨도를 구한 값과, 
### 'SalePrice'컬럼을 스케일링(log1p)로 변환한 이후 
### 왜도와 첨도를 구해 모두 더한 다음 소수점 2째자리까지 출력하시오

# 라이브러리 불러오기
import pandas as pd
import numpy as np

# 데이터셋 가져오기
dt = pd.read_csv("train.csv")

# SalePrice 컬럼의 왜도와 첨도 값 구하기
c = dt['SalePrice'].skew()
d = dt['SalePrice'].kurt()

# SalePrice 컬럼 로그변환
dt['SalePrice'] = np.log1p(dt['SalePrice'])
a = dt['SalePrice'].skew()
b = dt['SalePrice'].kurt()

print(round(a+b+c+d, 2))
