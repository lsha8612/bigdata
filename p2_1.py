import pandas as pd
import numpy as np
from itertools import combinations
from scipy.stats import pearsonr
import seaborn as sns
from statsmodels.stats.proportion import proportion_confint


### 1번. 데이터에서 'Attrition'은 퇴사여부에 대한 종속변수에 해당한다. 종속변수의 값을 다음과 같이 
### 수치로 변환해 새 컬럼으로 추가하고 각 범주별 레코드 수를 계산하시오.(Yes->1, No->0)

df = pd.read_csv('HR-Employee-Attrition.csv')
target = {'Yes':1, 'No':0}
df['Attrition_numerical'] = df['Attrition'].apply(lambda x: target[x])
#print(df['Attrition_change'].value_counts())

### 2반. 데이터셋의 데이터타입별 컬럼 개수를 계산하고, 범주형 변수 중 유일한 값을 1개만 가지고 있는
### 컬럼을 찾아내어 그 변수를 데이터에서 제거하시오.

# print(df.info())
# 수치형 컬럼은 27개, 범주형 컬럼은 9개

cat_feat = df.select_dtypes('object', 'category').columns.values
df_cat = df[cat_feat].copy()
df_cat.nunique().sort_values()
# print(df_cat.nunique())
df_cat = df_cat.drop(['Over18'], axis=1, errors='ignore')
# print(df.info())

### 3번. 원래 데이터에서 숫자형인 변수만 추출하여 새로운 데이터프레임을 생성하고,
### 각  변수간의 상관계수를 구하고 상관계수가 0.9 이상인 두 개의 컬럼을 찾아내어 그 변수 중 하나를 제거
num_feat = df.select_dtypes('number').columns.values
# 새로운 데이터 프레임 생성
attrition_num = df[num_feat].copy()
# print(attrition_num)
num_feat = attrition_num.columns.values
comb_num_feat = np.array(list(combinations(num_feat, 2)))
corr_num_feat = np.array([])

for comb in comb_num_feat:
    corr = pearsonr(attrition_num[comb[0]], attrition_num[comb[1]])[0]
    corr_num_feat = np.append(corr_num_feat, corr)

high_corr_num = comb_num_feat[np.abs(corr_num_feat) >= 0.9]
attrition_num = attrition_num.drop(np.unique(high_corr_num[:,0]), axis=1, errors='ignore')