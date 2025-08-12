import streamlit as st
import joblib

#導覽清單，要用 list
pg = st.navigation([
    st.Page('pages/p1.py', title='IRIS相關資訊',icon='🏷'),
    st.Page('pages/p2.py', title='IRIS品種預測',icon='💬')
]) 
pg.run()