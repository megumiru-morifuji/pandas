from flask import Flask,flash,render_template,request
import pandas as pd
from sklearn import tree
import pickle
import os

# Flaskアプリ作成
app=Flask(__name__)
# flashを使うための準備
app.secret_key = 'secret_key'

df=pd.read_csv('KvsT.csv')

head=df.head(3)
# print(head)

x_col=['身長','体重','年代']
x=df[x_col]
# print(x)

t=df['派閥']
# print(t)

# モデルの準備（未学習）
model=tree.DecisionTreeClassifier(random_state=0)

# 学習の実行
model.fit(x,t)

taro=[[170,70,20]]

# 新しいデータでの予測
taro_df=pd.DataFrame(taro,columns=x.columns)

# model.predict(taro_df)

result=model.score(x,t)
# print(result)

# print(os.getcwd())

# f=open('test.txt','r',encoding='utf-8')
# text=f.read()
# print(text)
# f.close()

# with open('kinokotakenoko.pkl','wb') as f:
#     pickle.dump(model,f)

with open('kinokotakenoko.pkl','rb') as f:
    model2=pickle.load(f)

suzuki=pd.DataFrame([[180,75,30]],columns=['身長','体重','年代'])
result=model2.predict(suzuki)
# print(result)

# ルート（URL）を定義
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/post',methods=['POST'])
def post():

    height=request.form['height']
    weight=request.form['weight']
    age=request.form['age']

    your_data=[[height,weight,age]]

    # 入力されたデータでデータフレームを作成
    your_data=pd.DataFrame(your_data,columns=x.columns)

    # 予測
    result=model.predict(your_data)
    result=result[0]
    print(result)

    if result=='きのこ':
        flash('あなたはきのこ派です')
    else:
        flash('あなたはたけのこ派です')
    
    return render_template('index.html')



# アプリを実行
if __name__=='__main__':
    app.run(debug=True)

