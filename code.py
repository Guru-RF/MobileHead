import busio
import board
import displayio
import digitalio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_sh1106
import rotaryio
import time

displayio.release_displays()

spi = busio.SPI(board.GP10, board.GP11)
display_bus = displayio.FourWire(
    spi,
    command=board.GP20,
    chip_select=board.GP21,
    reset=board.GP22,
    baudrate=1000000,
)

WIDTH = 128
HEIGHT = 64
BORDER = 5
display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

# Draw a label
text = "Hello World!"
text_area = label.Label(
    terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT // 2 - 1
)
splash.append(text_area)

knob = rotaryio.IncrementalEncoder(board.GP1, board.GP2)

button= digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# configure LEDs
bLED = digitalio.DigitalInOut(board.GP7)
bLED.direction = digitalio.Direction.OUTPUT
bLED.value = True

# configure LEDs
gLED = digitalio.DigitalInOut(board.GP8)
gLED.direction = digitalio.Direction.OUTPUT
gLED.value = True

# configure LEDs
rLED = digitalio.DigitalInOut(board.GP9)
rLED.direction = digitalio.Direction.OUTPUT
rLED.value = False


while True:
    print(knob.position)
    print(button.value)
    time.sleep(1)
    pass