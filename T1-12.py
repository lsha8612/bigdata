# 주어진 데이터에서 상위 10개 국가의 접종률 평균과 하위 10개 국가의 접종률 평균을 구하고, 그 차이를 구해보세요 
# (단, 100%가 넘는 접종률 제거, 소수 첫째자리까지 출력)

import pandas as pd
df = pd.read_csv("covid-vaccination-vs-death_ratio.csv")
df1 = df.groupby('country').max()
df1 = df1.sort_values(by='ratio', ascending=False)
df2 = df1[df1['ratio']<100]
print(df2)
upper = df2['ratio'].head(10).mean()
down = df2['ratio'].tail(10).mean()
print(round(upper-down, 1))