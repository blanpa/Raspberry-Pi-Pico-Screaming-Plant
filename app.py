import time
from grove.grove_moisture_sensor import GroveMoistureSensor
from grove.gpio import GPIO
import sys
import logging
from datetime import datetime
from grove.factory import Factory

# connect to alalog pin 2(slot A2)
sensor_moist = GroveMoistureSensor(2)

sensor_temp = Factory.getTemper("NTC-ADC", 2)

# Logging
logging.basicConfig(filename='logs.log', filemode='w', level=logging.DEBUG) 

def main():

    while True:
        # moist
        m = sensor_moist.moisture

        # Temp
        temp = sensor_temp.temperature

        # Motion Sensor
        Motion_value = GPIO(5, GPIO.IN)

        # Logs
        now = datetime.now()

        logs = f" Datetime: {now}, Moisture value: {m}, Temp value: {temp}, Motion_value: {Motion_value.read()}"
        logging.debug(logs)
        print(logs)

        time.sleep(1)

if __name__ == '__main__':
    main()