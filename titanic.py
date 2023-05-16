import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##깃허브의 타이타닉 데이터셋을 가져옴
df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

##vscode에서 출력하려면 print() 써야함
#print(df)

##데이터프레임 구조
#df.info()

##변수 타입 변환
df['Survived']=df['Survived'].astype(str)
df['Pclass']=df['Pclass'].astype(str)

##include=all을 사용하여 모든 변수에 대한 통계와 분포 출력
#print(df.describe(include='all'))

##Pclass별 탑승객의 수
#grouped=df.groupby('Pclass')
#print(grouped.size())

##요금 변수 분석
#plt.hist(df['Fare'])
#plt.show()

#data0=df[df['Survived']=='0']['Fare'] #사망자의 요금 데이터
#data1=df[df['Survived']=='1']['Fare'] #생존자의 요금 데이터
#fix, ax = plt.subplots()
#ax.boxplot([data0, data1])
#plt.show()

##성별 변수 분석
#group=df.groupby('Sex')
#print(group.size())

data0=df[df['Sex']=='female']['Survived']
group1=pd.DataFrame(data0).groupby('Survived')
print('여성 생존율')
print(group1.size())

data1=df[df['Sex']=='male']['Survived']
group2=pd.DataFrame(data1).groupby('Survived')
print('남성 생존율')
print(group2.size())