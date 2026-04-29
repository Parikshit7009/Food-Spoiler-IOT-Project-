import time
import sensors
import display
import logic
import buzzer

# Init
oled = display.init_oled()
dht_sensor, mq135 = sensors.init_sensors()

baseline = sensors.calibrate(mq135)

last_status = ""
last_time = 0

# Loop
while True:
    temp, hum = sensors.read_dht(dht_sensor)
    gas = sensors.read_gas(mq135)

    baseline = logic.update_baseline(baseline, gas)
    diff = gas - baseline

    status = logic.get_status(diff)

    last_time = buzzer.beep(status, last_status, last_time)

    print(temp, hum, gas, diff, status)

    display.show_data(oled, temp, hum, gas, status)

    last_status = status

    time.sleep(1)