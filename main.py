import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt


#data mininig

df = pd.read_csv('data.csv')
st.title('Data Analysis')

col1,col2,col3 = st.columns(3)
col1.metric('Year','$3652','$3528')
col2.metric('India','$3654','$3825')


df1 = df.drop(['ID','Year','Category','Product','UnitPrice','TotalPrice'],axis='columns')
st.write(df1)
# st.map(df1)

if st.button('Load Dataset'):st.write(df)
if st.sidebar.button('Load Description'):st.write(df.describe())
 
# st.dataframe(df,height =500,width = 800)
# st.table(df)

st.sidebar.button('Hello')


if st.sidebar.button('Load Bar Chart'):
    fig = plt.figure(figsize=(10,8))
    plt.bar(df['Year'],df['Product'])
    st.pyplot(fig)


a = {
    'name':['A','B','C'],
    'marks':[87,98,76]   
     }

# st.json(a)
st.table(a)


