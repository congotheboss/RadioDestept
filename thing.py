import threading
import time

import RPi.GPIO as GPIO
import Adafruit_DHT

LEDv_PIN = 19
LED_PIN = 13
DHT_TYPE    = Adafruit_DHT.DHT11
DHT_PIN     = 26

class PiThing(object):

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LEDv_PIN, GPIO.OUT)
        GPIO.setup(LEDr_PIN, GPIO.OUT)
        # Create a lock to syncronize access to hardware from multiple threads.
        self._lock = threading.Lock()
        # Setup a thread to read the DHT sensor every 2 seconds and store
        # its last known value.
        self._humidity = None
        self._temperature = None
        self._dht_thread = threading.Thread(target=self._update_dht)
        self._dht_thread.daemon = True  # Don't let this thread block exiting.
        self._dht_thread.start()
   
    def _update_dht(self):
        """Main function for DHT update thread, will grab new temp & humidity
        values every two seconds.
        """
        while True:
            with self._lock:
                # Read the humidity and temperature from the DHT sensor.
                self._humidity, self._temperature = Adafruit_DHT.read_retry(DHT_TYPE, DHT_PIN)
            # Wait 15 seconds then repeat.
            time.sleep(5.0)

    def get_humidity(self):
        """Get the most recent humidity value (%)."""
        with self._lock:
            return self._humidity

    def get_temperature(self):
        """Get the most recent temperature value (in degrees Celsius)."""
        with self._lock:
            return self._temperature

    def set_led(self, value):
        
        GPIO.output(LED_PIN, value)

    def set_ledv(self, value):
        GPIO.output(LEDv_PIN, value)