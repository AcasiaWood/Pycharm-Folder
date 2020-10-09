import Adafruit_SSD1306
import adafruit_mlx90614
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import board
import busio as io
import time

RST = None
x = 8
top = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, width, height), outline=0, fill=0)
font = ImageFont.truetype('NanumGothic.ttf', 14)
draw.text((x, top), "Temperature", font=font, fill=255)

while True:
    print("Ambient Temp: %d" % mlx.ambient_temperature)
    print("Object Temp: %d" % mlx.object_temperature)

    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    font = ImageFont.truetype('NanumGothic.ttf', 18)

    draw.text((x, top), "Temperature", font=font, fill=255)
    draw.text((x+20, top+35), str(round(mlx.object_temperature, 3))+"°C", font=font, fill=255)

    disp.image(image)
    disp.display()
    time.sleep(1)
