from machine import Pin
import time
import config

buzzer = Pin(config.BUZZER_PIN, Pin.OUT)

def beep(status, last_status, last_time):
    current_time = time.time()

    if status in ["WARNING", "SPOILED"]:
        if status != last_status or current_time - last_time > config.COOLDOWN:
            buzzer.value(1)
            time.sleep(0.3)
            buzzer.value(0)
            return current_time
    else:
        buzzer.value(0)

    return last_time