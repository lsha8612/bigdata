import pandas as pd

#df = pd.read_csv("https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/datasets/USJudgeRatings.csv")

#rint(df.head())

##왜도 계산을 위한 scipy 패키지의 scew() 함수 사용
import scipy.stats as ss

#print(ss.skew(df['CONT']))
#print(ss.skew(df['PHYS']))

##로그 변환
import numpy as np
#df['CONT1'] = np.log10(df['CONT'])
#df['PHYS1'] = np.log10(np.max(df['PHYS']+1)-df['PHYS'])

#print(ss.skew(df['CONT1']))
#print(ss.skew(df['PHYS1']))


##범주화, 이산형화
##임의로 데이터 생성
data = [['철수',52], ['영희',92], ['미영',84], ['시완',71], ['미경', 65],
        ['영환',81], ['숙경',66], ['부영',77], ['민섭',73], ['보연', 74], ['승하', 100]]

df = pd.DataFrame(data, columns=['이름', '수학점수'])
#print(df)
#print(np.mean(df['수학점수']))

##히스토그램, 범위 50~100, 5개 구간
import matplotlib.pyplot as plt
#plt.hist(df['수학점수'], bins=5, range=[50,100], rwidth=0.9)
#plt.show()

##조건을 사용해서 구간을 직접 지정
#df['등급'] = 0
#df.loc[(df['수학점수']<60), '등급'] = 'F'
#df.loc[(df['수학점수']>=60) & (df['수학점수']<70), '등급'] = 'D'
#df.loc[(df['수학점수']>=70) & (df['수학점수']<80), '등급'] = 'C'
#df.loc[(df['수학점수']>=80) & (df['수학점수']<90), '등급'] = 'B'
#df.loc[(df['수학점수']>=90) & (df['수학점수']<=100), '등급'] = 'A'

##cut()함수 사용
df['등급'] = pd.cut(x=df['수학점수'], bins=[0,60,70,80,90,100],
                  labels=['F','D','C','B','A'],
                  include_lowest=True)

##qcut() 함수 사용
df['등급_qcut'] = pd.qcut(x=df['수학점수'], q=5, labels=['F','D','C','B','A'])

print(df)