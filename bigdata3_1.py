### 모집단의 평균이 80일 때 일표본 t-검정(one-sample t-test)을 시행하여 평균값이 유의한지 확인

data = [75, 82, 80, 76, 84, 81, 79, 80, 78, 83, 74]

# 표본 평균값 구하기(반올림 셋째자리까지)
import numpy as np
m = round(np.mean(data), 3)
print(m)

# 위의 가설을 검증하기 위한 검정 통계량을 구하시오(반올림 둘째자리)
pop_mean = 80
from scipy.stats import ttest_1samp
t_statistic, p_value = ttest_1samp(data, pop_mean)
t_statistic =  round(t_statistic, 2)
print(t_statistic)

# 위의 통계량에 대한 p-값을 구하고 유의수준 0.05하에서 가설검정의 결과 중 하나 선택(반올림 넷째자리)
p_value = round(p_value, 4)
print(p_value)

# p_value는 0.4762로 0.05보다 크므로 귀무가설을 채택한다.
# 즉, 표본 학생들의 점수 평균은 80이라 보기 유의하다.