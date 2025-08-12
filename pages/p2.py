import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.title('IRIS品種預測')

st.image("iris.png")

#模型載入
svm = joblib.load('models/svm.joblib')
knn = joblib.load('models/Knn.joblib')
LR = joblib.load('models/LR.joblib')
rf = joblib.load('models/RF.joblib')

# 左側側邊攔：選擇模型
s1 = st.sidebar.selectbox('選擇模型', ['SVM', 'KNN', 'LogisticRegression', 'RandomForest'])

if s1 == 'SVM':
    model = svm
elif s1 == 'KNN':
    model = knn
elif s1 == 'LogisticRegression':
    model = LR
elif s1 == 'RandomForest':
    model = rf

#接收使用者輸入：4個特徵
df = pd.read_csv('iris.csv')
se1 = st.slider('花萼長度(cm)',
                float(df['sepal.length'].min())-0.5,
                float(df['sepal.length'].max())+0.8,
                float(df['sepal.length'].mean()))

se2 = st.slider('花萼寬度(cm)',
                float(df['sepal.width'].min())-0.5,
                float(df['sepal.width'].max())+0.8,
                float(df['sepal.width'].mean()))

se3 = st.slider('花辦長度(cm)',
                float(df['petal.length'].min())-0.5,
                float(df['petal.length'].max())+0.8,
                float(df['petal.length'].mean()))

se4 = st.slider('花辦長度(cm)',
                float(df['petal.width'].min())-0.5,
                float(df['petal.width'].max())+0.8,
                float(df['petal.width'].mean()))

labels = ['Setosa', 'Versicolor', 'Viraginica']

if st.button('進行預測'):
    X = np.array([[se1, se2, se3, se4]])
    y = model.predict(X)
    st.write(f'### 預測結果：{y}')
    st.write(f'### 品種名稱：{labels[y[0]]}')