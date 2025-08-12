import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('IRIS相關資訊')
df = pd.read_csv('iris.csv')
st.write(df.head())# 展示前 5 筆 data

st.write('### IRIS樣品散步圖')

mapping = {'Setosa':0, 'Versicolor':1, 'Virginica':2}
colors=['red', 'green', 'blue']

# 依 Tab 顯示不同的欄位的分布情況
tab1, tab2 = st.tabs(['[依花萼長寬]', '[依花瓣長寬]'])

fig1, ax1 = plt.subplots()
with tab1:
    for i, s in mapping.items():
        subset = df[df['variety'] ==i]
        ax1.scatter(subset['sepal.length'], subset['sepal.width'], label=i, c=colors[s])
    ax1.set_xlabel('sepal.length')
    ax1.set_ylabel('sepal.width')
    ax1.legend()
    st.pyplot(fig1)

fig2, ax2 = plt.subplots() 
with tab2:
    for i, s in mapping.items():
        subset = df[df['variety'] ==i]
        ax2.scatter(subset['petal.length'], subset['petal.width'], label=i, c=colors[s])
    ax2.set_xlabel('petal.length')
    ax2.set_ylabel('petal.width')
    ax2.legend()
    st.pyplot(fig2)