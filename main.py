import blinkt
import busio
from adafruit_is31fl3731.charlie_plex import CharliePlex as Display

blinkt.set_all(255, 255, 255, 0.1)
blinkt.show()
print("Set color for blinkt")

i2c = busio.I2C(board.SCL, board.SDA)
display = Display(i2c)
display.pixel(0, 0, 10)
print("Set color for adafruit charlieplex")
