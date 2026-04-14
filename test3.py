import pandas as pd
from sklearn import tree
import pickle

df=pd.read_csv('iris.csv')
# print(df.head(3))
# print(df['種類'].unique())
# 
# print(df.sum())

# tmp=df.isnull()
# tmp=tmp.sum()
# print(tmp)

# df2=df.dropna(how='any',axis='0')
colmean=df['花弁幅'].mean(numeric_only=True)
df2=df.fillna(colmean)
print(df2.isnull())