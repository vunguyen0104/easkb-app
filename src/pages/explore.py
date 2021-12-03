import streamlit as st
import pyodbc
import src.share.environment as env
import pandas as pd
import matplotlib.pyplot as plt

server = env.DB_HOST
database = env.DB_NAME 
username = env.DB_USER 
password = env.DB_PASS

@st.cache
def load_data():
    query = "SELECT * FROM VW_KnowledgeBaseCategoryByMonth"
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    data = pd.read_sql(query, conn)

    return data

df = load_data()

def show_explore_page():
    st.title(":bar_chart: Explore Page")

    data = df["CategoryDescription"].value_counts()

    fig1, ax1 = plt.subplots(1,1, figsize=(12, 7))
    #ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.pie(data, labels=data.index, autopct="%.0f%%", shadow=False, startangle=0, textprops={'size': 'smaller'})
    ax1.axis("equal")

    st.write("""
        #### Number of Categories
    """)

    st.pyplot(fig1)

    st.write("""
        #### Total of Knowledge Bases By Category
    """)

    data = load_data()

    data = df.groupby(["CategoryDescription"])["KnowledgeBaseCount"].sum().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""
        #### Total of Knowledge Bases By Month
    """)

    data = df.groupby(["CreatedMonth"])["KnowledgeBaseCount"].sum().sort_values(ascending=True)
    st.line_chart(data)


