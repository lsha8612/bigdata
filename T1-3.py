### 주어진 데이터에서 결측치가 80%이상 되는 컬럼은(변수는) 삭제하고, 
### 80% 미만인 결측치가 있는 컬럼은 'city'별 중앙값으로 값을 대체하고 
### 'f1'컬럼의 평균값을 출력하세요!

# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv("basic1.csv")

# 결측값(비율) 확인
# print((df.isnull().sum() / df.shape[0]))

# 결측치가 80% 이상인 컬럼 삭제
df = df.drop(['f3'], axis=1)

# city별 중앙값 계산
# print(df['city'].unique())
a = df[df['city']=='서울']['f1'].median()
b = df[df['city']=='경기']['f1'].median()
c = df[df['city']=='부산']['f1'].median()
d = df[df['city']=='대구']['f1'].median()

# f1 결측치 city별 중앙값으로 대체
df['f1'] = df['f1'].fillna(df['city'].map({'서울':a, '경기':b,
                                           '부산':c, '대구':d}))
print(df['f1'].mean())

