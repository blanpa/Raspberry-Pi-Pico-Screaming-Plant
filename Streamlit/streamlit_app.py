import streamlit as st
import time  # to simulate a real time data, time loop

# data
import pandas as pd

# database
import sqlalchemy as sqla
import snowflake.connector

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

# Initialize connection.
# Uses st.experimental_singleton to only run once.


@st.experimental_singleton
def init_connection():
    return snowflake.connector.connect(**st.secrets["snowflake"])


conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.


@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        # return cur.fetchall()
        return cur.fetch_pandas_all()


def main():
    st.title("IOT-Topfpflanze")

    # engine_db = sqla.create_engine(st.secrets.db_credentials.database)

    anzahl = st.number_input(label="", min_value=100,
                             max_value=100000, value=2000)

    statement = f""" 
    SELECT * FROM PLANTDATA_TEST.PFLANZENDATEN.TEST ORDER BY ts DESC LIMIT {anzahl};
    """
    #st.text_input(label = "SQL Query", value= statement )

    placeholder = st.empty()

    while True:
        df = run_query(statement)

        with placeholder.container():
            kpi1, kpi2, kpi3 = st.columns(3)

            kpi1.metric(
                label="Temperature",
                value=df["temp_value"].mean(),
                delta=0,
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

            data_col1, data_col2 = st.columns(2)

            with data_col1:
                st.subheader("Detailed Data View")
                st.write(df)

            with data_col2:
                st.subheader("Data")
                st.write(df.describe())

            # Query wird wird alle zwei Sekunden neu geladen um neue Darten darzustellen
            time.sleep(2)


if __name__ == "__main__":
    main()
