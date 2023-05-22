import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

#print(df.isnull().sum())
#print(df.info())

##결측치가 있는 행 전체 삭제
df_1 = df.dropna(axis=0)
print(df_1.isnull().sum().sum())
print(df_1.shape)

##결측치를 지정값으로 대체(Age변수-평균값으로 대체)
print(df['Age'].isnull().sum())
mean = df['Age'].mean()
df['Age'].fillna(mean, inplace=True)
print(df['Age'].isnull().sum())

##결측치를 지정값으로 대체(Embarked변수-최빈값으로 대체)
from scipy.stats import mode

print(df['Embarked'].isnull().sum())
embarked_mode = df['Embarked'].mode()
df['Embarked'].fillna(embarked_mode[0], inplace=True)
print(df['Embarked'].isnull().sum())

##결측치를 그룹별 평균값으로 대체
df1 = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
print(df1.groupby('Sex')['Age'].mean())
print(df1.groupby('Pclass')['Age'].mean())
df1['Age'].fillna(df.groupby('Pclass')['Age'].transform('mean'), inplace=True)
print(df1['Age'].tail())