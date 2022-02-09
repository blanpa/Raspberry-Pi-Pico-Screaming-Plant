import time
from grove.grove_moisture_sensor import GroveMoistureSensor
import seeed_dht
from grove.gpio import GPIO
import sys

# connect to alalog pin 2(slot A2)
PIN = 2
sensor_moist = GroveMoistureSensor(PIN)
sensor_temp = seeed_dht.DHT("11", 12)

class GroveMiniPIRMotionSensor(GPIO):
    def __init__(self, pin):
        super(GroveMiniPIRMotionSensor, self).__init__(pin, GPIO.IN)
        self._on_detect = None
 
    @property
    def on_detect(self):
        return self._on_detect
 
    @on_detect.setter
    def on_detect(self, callback):
        if not callable(callback):
            return
 
        if self.on_event is None:
            self.on_event = self._handle_event
 
        self._on_detect = callback
 
    def _handle_event(self, pin, value):
        if value:
            if callable(self._on_detect):
                self._on_detect()
 
#Grove = GroveMiniPIRMotionSensor

def main():
    while True:
        # moist
        m = sensor_moist.moisture
        if 0 <= m and m < 300:
            result = 'Dry'
        elif 300 <= m and m < 600:
            result = 'Moist'
        else:
            result = 'Wet'
        print('Moisture value: {0}, {1}'.format(m, result))
        time.sleep(1)

        #Temp and humi
        humi, temp = sensor_temp.read()

        #PIR
        if len(sys.argv) < 2:
            print('Usage: {} pin'.format(sys.argv[0]))
            sys.exit(1)
    
        pir = GroveMiniPIRMotionSensor(int(sys.argv[1]))
    
        def callback():
            print('Motion detected.')
    
        pir.on_detect = callback
    

        time.sleep(1)

if __name__ == '__main__':
    main()