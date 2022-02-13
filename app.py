import time
from grove.grove_moisture_sensor import GroveMoistureSensor
#import seeed_dht
from grove.gpio import GPIO
import sys
import logging
from datetime import datetime

# connect to alalog pin 2(slot A2)
sensor_moist = GroveMoistureSensor(2)

# sensor_temp = seeed_dht.DHT("11", 12)

# Logging
logging.basicConfig(filename='logs.log', filemode='w', level=logging.DEBUG) 

def main():

    while True:
        # moist
        m = sensor_moist.moisture

        #Temp and humi
        # humi, temp = sensor_temp.read()

        # Motion Sensor
        Motion_value = GPIO(5, GPIO.IN)

        # Logs
        now = datetime.now()

        logs = f" Datetime: {now}, Moisture value: {m}, Humi value:{0}, Temp value: {0}, Motion_value: {Motion_value.read()}"
        logging.debug(logs)
        print(logs)

        time.sleep(1)

if __name__ == '__main__':
    main()