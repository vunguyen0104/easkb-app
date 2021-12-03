import streamlit as st
import pyodbc
import src.share.environment as env
import pandas as pd

server = env.DB_HOST
database = env.DB_NAME 
username = env.DB_USER 
password = env.DB_PASS

@st.cache
def load_data(category):
    query = "SELECT * FROM VW_KnowledgeBaseCategoryByMonth WHERE CategoryDescription = ?"
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    data = pd.read_sql(query, conn, params=(category,))

    return data

def show_display_page():
    st.title("Knowledge Base Categories")

    categories = (
        "Application",
        "Database",
        "Documentation",
        "FTP / SFTP",
        "Import / Export Data",
        "Java",
        "Javascript",
        "Linux",
        "MSSQL Server",
        "Network",
        "Oracle",
        "Other",
        "Processing Job",
        "Report",
        "REST API",
        "SharePoint",
        "Spring Framework",
        "Swift",
        "Troubleshooting Issue",
        "Version Control",
        "Virtualization",
        "Web Services",
        "Windows Server"
    )

    category = st.sidebar.selectbox("Category", categories)

    data = load_data(category)
    st.dataframe(data)

