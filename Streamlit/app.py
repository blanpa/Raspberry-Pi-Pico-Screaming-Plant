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
    
    #engine_db = sqla.create_engine(secret)
    engine_db = sqla.create_engine(st.secrets.db_credentials.database)



    statement = """ 
    SELECT * FROM testtest2 ORDER BY ts DESC LIMIT 1000;
    """

    placeholder = st.empty()

    while True:
        df = pd.read_sql(statement, con = engine_db)

        with placeholder.container():
            kpi1, kpi2, kpi3 = st.columns(3)

            kpi1.metric(
                label="Temperature",
                value=df["temp_value"].mean(),
                delta= 0,
            )
            
            kpi2.metric(
                label="Moisture",
                value=df["moisture_value"].mean(),
                delta=0,
            )
            
            kpi3.metric(
                label="Movement",
                value=df["motion_value"].mean(),
                delta=0,
            )

            fig_col1, fig_col2, fig_col3 = st.columns(3)

            with fig_col1:
                st.markdown("### temp_value")
                fig = px.line(df, y='temp_value', x="ts")
                st.write(fig)
            
            with fig_col2:
                st.markdown("### moisture_value")
                fig2 = px.line(df, y='moisture_value', x="ts")
                st.write(fig2)
            
            with fig_col3:
                st.markdown("### motion_value")
                fig3 = px.line(df, y='motion_value', x="ts")
                st.write(fig3)

            st.subheader("Detailed Data View")
            st.write(df)
            time.sleep(5)
            




if __name__ == "__main__":
    main()