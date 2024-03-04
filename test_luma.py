import time

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
# from luma.core.virtual import viewport, terminal
from luma.led_matrix.device import max7219
from PIL import ImageFont

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)

font = ImageFont.truetype("pixelmix.ttf", 8)
text = "hello"
position = (0, 0)
fill="white"

with canvas(device) as draw:
    draw.text(position, text, fill=fill, font=font)

time.sleep(20)
