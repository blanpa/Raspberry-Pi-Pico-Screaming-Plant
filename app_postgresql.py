# Import all needed libarys
import time
from grove.grove_moisture_sensor import GroveMoistureSensor
from grove.gpio import GPIO
import sys
import logging
from datetime import datetime
#import playsound
#from grove.factory import Factory
import psycopg2
import os
import sysconfig
import math
from grove.adc import ADC
import numpy as np

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

# Database Connection
conn = psycopg2.connect(
    dbname="rlruqohb",
    user="rlruqohb",
    password=PASSWORD,
    host="	hattie.db.elephantsql.com", port="5432")

conn.autocommit = True

# Connect to Moisture Sensor, connect to alalog pin 2(slot A2)
sensor_moist = GroveMoistureSensor(0)

# Connect to Temp Sensor, workaround
#sensor_temp = Factory.getTemper("NTC-ADC", 2)
sensor_temp = GroveMoistureSensor(2)
B = 4275  # B value of the thermistor
R0 = 100000  # R0 = 100k

# Define Logging
logging.basicConfig(filename='logs.log', filemode='w', level=logging.DEBUG)


def main():

    while True:
        # moist
        moist_value = sensor_moist.moisture

        # Temp
        a = sensor_temp.moisture
        R = 3500.0 / float(a) - 1.0  # 1023.0
        R = R0*R
        temp_value = 1.0/(np.log(R/R0)/B+1/298.15)-273.15

        # Motion Sensor
        motion = GPIO(5, GPIO.IN)
        motion_value = motion.read()

        if motion_value == True:
            pass
            # if moist > 100:
            #     playsound.playsound('test.mp3', False)

            # if moist <= 100:
            #     playsound.playsound('test.mp3', False)

        # Value for Logs
        now = datetime.now()

        logs = f" python_datetime: {now}, moisture_value: {moist_value}, temp_value: {temp_value}, motion_value: {motion_value}"
        # logging.debug(logs)
        # print(logs)

        # # Database plant_times_series_data
        cursor = conn.cursor()
        statement = f""" 
        INSERT INTO plantdb_table_1
        VALUES(
            CURRENT_TIMESTAMP,
            {moist_value},
            {temp_value},
            {motion_value});
        """
        cursor.execute(statement)

        conn.commit()
        # conn.close()

        # Sleep for 1 Second, we dont want to get to much data
        time.sleep(2)


if __name__ == '__main__':
    main()
