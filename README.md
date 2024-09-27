# rp2040-ssd1306-diag
A MicroPython program to test readings from RP2040's ADCs and print them out on the SSD1306 128x64 OLED screen.

Tested with Lena Kryger's [RP1](https://lenakryger.de/rp1); should also at the very least work with Raspberry Pi Pico and pyboard. 

![Image](<https://raw.githubusercontent.com/MariaWasNotAvailable/rp2040-ssd1306-diag/refs/heads/main/oled.webp>)

# Usage
1. Flash MicroPython onto the board (recommended tool: [Thonny](https://thonny.org))
2. Copy the SSD1306 driver (recommended build: [stlehmann's](https://github.com/stlehmann/micropython-ssd1306))
3. Copy the main.py file

Don't forget to connect the display to the board! The ```pins/resolution/sleep_length``` values should be self-explanatory and easy to edit, but the default pin configuration is SCL=5, SDA=4.
