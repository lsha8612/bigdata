### p2.csv 파일에는 95명에 대한 데이터가 있다.
### 평균키는 165cm라 판단할 수 있는지 귀무가설과 대립가설을 설정한 후
### 유의수준 5%로 검정하고자 한다.

# 정규성 여부를 판단하고자 한다. Shapiro 검정 통계량을 구하시오.(소수점 셋째자리)
from scipy.stats import shapiro
import pandas as pd
p2 = pd.read_csv("p2.csv")

static, value = shapiro(p2)
static = round(static, 3)
print(static)

# Shapiro 검정 p-값을 구하고 정규성 여부에 대해 유의수준 0.05로 검정(반올림, 3)
vlaue = round(value, 3)
print(value)
# 0.638로 0.05 이상이므로 귀무가설을 기각하지 않음, 데이터는 정규성 만족

# 데이터의 평균키는 165cm라고 할 수 있는지 일표본 t-검정을 시행하고 검정량을 소수점 이하 3자리로 구하시오.
from scipy.stats import ttest_1samp
teststatic, pvalue = ttest_1samp(p2['height'], 165)
teststatic = round(teststatic, 3)
print(teststatic)