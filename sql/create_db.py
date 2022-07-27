import psycopg2
# https://stackoverflow.com/questions/55755095/postgresql-modulenotfounderror-no-module-named-psycopg2
import sysconfig
import os

# from sqlalchemy import create_engine
print(sysconfig.get_platform())

try:
    if sysconfig.get_platform() == "linux-armv7l":
        path = os.path.join("/home", "pi", "Code", "Confidental", "psswd.txt")
        PASSWORD = open(path, mode="r").read()
    else:
        PASSWORD = open(os.path.join("..", "Confidental",
                        "passwd.txt"), mode="r").read()

    print("Got the right Password")
except:
    print(path)
    print("Password is not in the Confidental Directory!")
    exit()


conn = psycopg2.connect(
    dbname="rlruqohb",
    user="rlruqohb",
    password=PASSWORD,
    host="	hattie.db.elephantsql.com", port="5432")

conn.autocommit = True

cursor = conn.cursor()

statement = """ 
CREATE TABLE plantdb_table_1 (
	ts timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
	moisture_value FLOAT4 NULL,
	temp_value FLOAT4 NULL,
	motion_value FLOAT4 NULL);
"""
# SELECT create_hypertable('tbl_xyz', 'ts');

# plant_times_series_data
#	uuid uuid NULL,

cursor.execute(statement)

conn.commit()
print(statement)
conn.close()
