from machine import Pin, I2C, ADC
import dht
import time
import ssd1306

# ---------------- I2C SETUP ----------------
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
devices = i2c.scan()
print("I2C devices:", devices)

oled = None
if len(devices) > 0:
    addr = devices[0]
    print("OLED found at:", hex(addr))
    oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=addr)
else:
    print("No OLED detected!")

# ---------------- SENSORS ----------------
dht_sensor = dht.DHT22(Pin(14))   # DHT22 on GP14
mq135 = ADC(26)
buzzer = Pin(15, Pin.OUT)         # Buzzer on GP15

# ---------------- CALIBRATION ----------------
if oled:
    oled.fill(0)
    oled.text("Calibrating...", 0, 20)
    oled.show()

time.sleep(2)

baseline = 0
for i in range(10):   # faster calibration
    baseline += mq135.read_u16()
    time.sleep(0.2)

baseline = baseline // 10
print("Baseline:", baseline)

# ---------------- VARIABLES ----------------
last_status = ""
last_beep_time = 0
cooldown = 5   # faster beep repeat

# ---------------- MAIN LOOP ----------------
while True:
    try:
        # ---- DHT22 READ ----
        try:
            time.sleep(1)
            dht_sensor.measure()
            temp = dht_sensor.temperature()
            hum = dht_sensor.humidity()
        except:
            temp = 0
            hum = 0

        # ---- GAS READ ----
        gas = mq135.read_u16()
        time.sleep(0.1)
        gas = (gas + mq135.read_u16()) // 2

        diff = max(0, gas - baseline)

        # ---- FAST LOGIC ----
        if diff > 60:
            status = "SPOILED"
        elif diff > 15:
            status = "WARNING"
        else:
            status = "SAFE"

        # ---- BUZZER (WARNING + SPOILED) ----
        current_time = time.time()

        if status in ["WARNING", "SPOILED"]:
            if (last_status != status) or (current_time - last_beep_time > cooldown):
                buzzer.value(1)
                time.sleep(0.2)
                buzzer.value(0)
                last_beep_time = current_time
        else:
            buzzer.value(0)

        last_status = status

        # ---- DEBUG ----
        print("Temp:", temp, "Hum:", hum)
        print("Gas:", gas, "Baseline:", baseline, "Diff:", diff)
        print("Status:", status)
        print("----------------------")

        # ---- OLED DISPLAY ----
        if oled:
            oled.fill(0)
            oled.text("FridgeGuard", 10, 0)
            oled.text("Temp:{}C".format(temp), 0, 15)
            oled.text("Hum:{}%".format(hum), 0, 25)
            oled.text("Gas:{}".format(gas), 0, 35)
            oled.text(status, 40, 55)
            oled.show()

    except Exception as e:
        print("Error:", e)
        buzzer.value(0)

        if oled:
            oled.fill(0)
            oled.text("Sensor Error!", 0, 30)
            oled.show()

        time.sleep(1)
        