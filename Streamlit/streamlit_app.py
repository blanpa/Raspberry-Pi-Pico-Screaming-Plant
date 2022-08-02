import streamlit as st
import time  # to simulate a real time data, time loop

# data
import pandas as pd

# database
import sqlalchemy as sqla
# import snowflake.connector

# Viz
import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts

import numpy as np
import pytz
from datetime import datetime
from datetime import date
from PIL import Image
from local_wather import *
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="Real-Time Plant Dashboard",
    page_icon="🪴",
    layout="wide",
)

st.title("Real-Time Plant Dashboard")
# Autorefresh:
count = st_autorefresh(interval=10000, limit=1000, key="fizzbuzzcounter")

# Initialize connection.
# Uses st.experimental_singleton to only run once.


# @st.experimental_singleton
# def init_connection():
#     return snowflake.connector.connect(**st.secrets["snowflake"])


# conn = init_connection()

# # Perform query.
# # Uses st.experimental_memo to only rerun when the query changes or after 10 min.


# @st.experimental_memo(ttl=600)
# def run_query(query):
#     with conn.cursor() as cur:
#         cur.execute(query)
#         # return cur.fetchall()
#         return cur.fetch_pandas_all()

# Time
nowTime = datetime.now()
current_time = nowTime.strftime("%H:%M:%S")
today = str(date.today())
timeMetric, = st.columns(1)

engine_db = sqla.create_engine(st.secrets.db_credentials.database)

statement = f""" 
SELECT * FROM "public"."plantdb_table_1" ORDER BY ts DESC LIMIT {4000};
"""
#st.text_input(label = "SQL Query", value= statement )

# Row A
a1, a2, a3, a4, a5, a6 = st.columns(6)
a1.metric("Current Temperature", f"{get_temp()}", f"{temp_difference()}"+"%")
a2.metric("Current time", f"{current_time}")
a3.metric("Humidity", f"{get_humidity()}"+"%")
a4.metric("Feels like", f"{get_feel()}")
a5.metric("Highest temperature", f"{get_temp_max()}")
a6.metric("Lowest temperature", f"{get_temp_min()}")


placeholder = st.empty()

# df = run_query(statement)
df = pd.read_sql_query(statement, engine_db)

with placeholder.container():
    kpi1, kpi2, kpi3 = st.columns(3)

    kpi1.metric(
        label="Temperature Sensor",
        value=df["temp_value"][0],
        delta=df["temp_value"][1]-df["temp_value"][0],
    )

    kpi2.metric(
        label="Moisture Sensor",
        value=df["moisture_value"][0],
        delta=df["moisture_value"][1]-df["moisture_value"][0],
    )

    kpi3.metric(
        label="Movement Sensor",
        value=df["motion_value"][0],
        delta=df["motion_value"][1]-df["motion_value"][0],
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

data_col1, data_col2, data_col3 = st.columns(3)

# with data_col1:
#     st.subheader("Moisture Forecast")

#     pass

# with data_col2:
#     st.subheader("Detailed Data View")
#     st.write(df)

# with data_col3:
#     st.subheader("Data")
#     st.write(df.describe())


# def main():
#    pass
# if __name__ == "__main__":
#    main()
