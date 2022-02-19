import psycopg2

# from sqlalchemy import create_engine

conn = psycopg2.connect(
    dbname="plantdb", 
    user="pi", 
    password="", 
    host="localhost", port ="5432")

conn.autocommit = True

cursor = conn.cursor()

statement = """ 
CREATE TABLE plant_times_series_data (
	ts timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
	uuid uuid NULL,
	python_datetime int4 NULL,
	moisture_value int4 NULL,
	temp_value int4 NULL,
	motion_value int4 NULL);

SELECT create_hypertable('tbl_xyz', 'ts');

"""

cursor.execute(statement)
  
conn.commit()
conn.close()
