import pandas as pd
from sklearn import tree
import pickle

# data=[
#     [70,80],
#     [72,85],
#     [75,79],
#     [80,92]
# ]
# df=pd.DataFrame(data,columns=['データベースの試験得点','ネットワークの試験得点'])
# # print(df)

# df.index=['一郎','次郎','三郎','太郎']


df=pd.read_csv('ex1.csv')
# df=df.columns

col=['x0','x2']

print(df[col])

# print(df)