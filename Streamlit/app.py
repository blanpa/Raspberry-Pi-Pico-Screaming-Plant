import streamlit as st
import time # to simulate a real time data, time loop

# data
import pandas as pd

# database
import sqlalchemy as sqla

# Viz
import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts


st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)
def main():
    st.title("Pascals real-time live Dashboard with IOT-Topfpflanze")


    #conn = psycopg2.connect(
    #    database= st.secrets.db_credentials.database,
    #    user= st.secrets.db_credentials.user,
    #    password= st.secrets.db_credentials.password,
    #    host= st.secrets.db_credentials.host,
    #    )
    
    engine_db = sqla.create_engine(st.secrets.db_credentials.database)



    kpi1, kpi2, kpi3 = st.columns(3)

    fig_col1, fig_col2 = st.columns(2)


    statement = """ 
    SELECT * FROM testtest2 ORDER BY ts DESC LIMIT 1000;
    """

    while True:
        DF = pd.read_sql(Eintrag, con = engine_db)


        st.subheader("Detailed Data View")
        st.write(df)
        time.sleep(5)



if __name__ == "__main__":
    main()