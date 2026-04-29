from machine import Pin, ADC
import dht
import time
import config

def init_sensors():
    dht_sensor = dht.DHT22(Pin(config.DHT_PIN))
    mq135 = ADC(config.MQ135_PIN)
    return dht_sensor, mq135

def read_dht(sensor):
    try:
        sensor.measure()
        return sensor.temperature(), sensor.humidity()
    except:
        return 0, 0

def read_gas(mq135):
    return (mq135.read_u16() + mq135.read_u16()) // 2

def calibrate(mq135):
    baseline = 0
    for _ in range(20):
        baseline += mq135.read_u16()
        time.sleep(0.1)
    return baseline // 20