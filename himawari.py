import ctypes
from typing import List
import requests
from PIL import Image
from io import BytesIO
import datetime
import time
import pathlib

# 1, 2, 4, 8
dim = 4

t = datetime.datetime.now()

# Snap to closest 10 minuts
t -= datetime.timedelta(minutes=t.minute % 10)

# Convert time to GMT 0
t -= datetime.timedelta(hours=9, minutes=20)

# GMT +2
t -= datetime.timedelta(hours=2)

path = f"https://himawari8-dl.nict.go.jp/himawari8/img/D531106/{dim}d/550/{t.strftime('%Y/%m/%d/%H%M00')}"

imgs: List[List[Image.Image]] = []
for x in range(dim):
	imgs.append(list())
	for y in range(dim):

		url = path + f"_{x}_{y}.png"
		print(url)

		response = requests.get(url)
		imgs[x].append(Image.open(BytesIO(response.content)))


w, h = imgs[0][0].size
img = Image.new("RGB", (w * dim, h * dim))
for x in range(dim):
	for y in range(dim):
		img.paste(imgs[x][y], (x * w, y * h, (x + 1) * w, (y + 1) * h))


directory = str(pathlib.Path(__file__).parent.resolve())
img_path = directory + "\\lastest.png"

img.save(img_path)
img.close()

time.sleep(5)

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, img_path, 0)