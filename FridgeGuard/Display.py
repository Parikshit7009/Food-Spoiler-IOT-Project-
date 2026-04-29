from machine import Pin, I2C
import ssd1306
import config

def init_oled():
    i2c = I2C(0, scl=Pin(config.I2C_SCL), sda=Pin(config.I2C_SDA))
    devices = i2c.scan()

    if devices:
        return ssd1306.SSD1306_I2C(128, 64, i2c, addr=devices[0])
    return None

def show_data(oled, temp, hum, gas, status):
    if oled:
        oled.fill(0)
        oled.text("FridgeGuard", 10, 0)
        oled.text(f"T:{temp}C", 0, 15)
        oled.text(f"H:{hum}%", 0, 25)
        oled.text(f"G:{gas}", 0, 35)
        oled.text(status, 40, 55)
        oled.show()