import streamlit as st
import time

# data
import pandas as pd

# database
import sqlalchemy as sqla
import psycopg2

# Viz
import plotly as py

st.header("Pascals real-time live Dashboard with IOT-Topfpflanze")

def main():

    #conn = psycopg2.connect(
    #    database= st.secrets.db_credentials.database,
    #    user= st.secrets.db_credentials.user,
    #    password= st.secrets.db_credentials.password,
    #    host= st.secrets.db_credentials.host,
    #    )
    
    engine_db = sqla.create_engine(st.secrets.db_credentials.database)

    statement = """ 
    SELECT * FROM testtest2 ORDER BY ts DESC LIMIT 1000;
    """

    while True:
        DF = pd.read_sql(Eintrag, con = engine_db)
        st.write(df)
        time.sleep(5)



if name == __main__:
    main()