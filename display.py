import time

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas

# from luma.core.virtual import viewport, terminal
from luma.led_matrix.device import max7219
from PIL import ImageFont


class Display:
    def __init__(self):
        serial = spi(port=0, device=0, gpio=noop())
        self.device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)
        self.font = ImageFont.truetype("pixelmix.ttf", 8)
        self.position = (0, 0)
        self.text_color = "white"

    def write(self, text):
        with canvas(self.device) as draw:
            draw.text(self.position, text, fill=self.text_color, font=self.font)
