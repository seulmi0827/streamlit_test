import streamlit as st
import pymysql
from pymysql.cursors import DictCursor 
import pandas as pd


st.title('베포 데스트')
st.write('hello')

conn = pymysql.connect(
    host = 'localhost',
    port = 3307,
    user = 'root',
    password = 'test1234',
    database = 'study',
    charset = 'utf8mb4'
)

def load_data():
    with conn.cursor(cursor=DictCursor) as cur:
        cur.execute('SELECT * FROM orders')
        return pd.DataFrame(cur.fetchall())
    
df = load_data()

st.dataframe(df)