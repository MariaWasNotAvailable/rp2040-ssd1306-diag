from machine import Pin, SoftI2C, ADC
import ssd1306
import time

pins = [5,4]
resolution = [128,64]
sleep_length = 1

i2c = SoftI2C(scl=Pin(pins[0]), sda=Pin(pins[1]))
display = ssd1306.SSD1306_I2C(resolution[0], resolution[1], i2c)

def read_volt(pin):
    adc_value = ADC(pin).read_u16()
    volt = (3.3/65535) * adc_value

    return volt

def read_raw(pin):
    return round(ADC(pin).read_u16()//1000)

def convert_to_celsius(volt):
    return round(27 - (volt - 0.706)/0.001721, 1)

while True:
    display.fill(0)

    display.text(f"Temp: {convert_to_celsius(read_volt(4))}'C", 0, 0)
    display.text(f"ADC 0: {round(read_volt(0),4)}V", 0, 9)
    display.text(f"ADC 1: {round(read_volt(1),4)}V", 0, 18)
    display.text(f"ADC 2: {round(read_volt(2),4)}V", 0, 27)
    display.text(f"ADC 3: {round(read_volt(3),4)}V", 0, 36)
    display.text("Raw(Temp/ADC0-3)", 0, 45)
    display.text(f"{read_raw(4)}/{read_raw(0)}/{read_raw(1)}/{read_raw(2)}/{read_raw(3)}k", 0, 54)

    display.show()

    time.sleep(sleep_length)
