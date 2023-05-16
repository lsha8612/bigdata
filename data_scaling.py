import numpy as np
import pandas as pd

#한국인, 일본인 각 성인 1000명 육류소비량 데이터 생성
korean = 5*np.random.randn(1000)+53.9 #평균은 53.9/표준편차는 5인 난수 1000개
japan = 4*np.random.randn(1000)+32.7 #평균은 32.7/표준편차는 4인 난수 1000개

df = pd.DataFrame({"한국인":korean, "일본인":japan})
print(df)