import os
import requests
from PIL import Image
from io import BytesIO
import datetime
import pathlib
import itertools
import pytz

from tqdm.contrib.concurrent import thread_map

# 1  = 550x550
# 2  = 1100x1100
# 4  = 2200x2200
# 8  = 4400x4400
# 16 = 8800x8800
# 20 = 11000x11000
dim = 8

# Get the current time
t = datetime.datetime.now().astimezone()

# Translated to UTC
t = t.astimezone(pytz.utc)

# Interpreted as JST
t = t.replace(tzinfo=pytz.timezone("Japan"))

# Make sure that there is an image available
if t >= datetime.datetime.now(pytz.timezone("Japan")):
    t -= datetime.timedelta(days=1)

# Translated to UTC
t = t.astimezone(pytz.utc)

# Snap to closest 10 minuts
t -= datetime.timedelta(minutes=t.minute % 10)

print(t)

size = 550
path = f"https://himawari8-dl.nict.go.jp/himawari8/img/D531106/{dim}d/{size}/{t.strftime('%Y/%m/%d/%H%M00')}"

coords = list(itertools.product(range(dim), range(dim)))
imgs: dict[tuple[int, int], Image.Image] = {}

def f(coord):
    url = path + f"_{coord[0]}_{coord[1]}.png"
    response = requests.get(url)
    imgs[coord] = Image.open(BytesIO(response.content))

r = thread_map(f, coords, desc="Downloading")

img = Image.new("RGB", (size * dim, size * dim))
for x, y in coords:
    img.paste(imgs[(x, y)], (x * size, y * size, (x + 1) * size, (y + 1) * size))


directory = str(pathlib.Path(__file__).parent.resolve())
img_path = os.path.join(directory, "lastest.png")

print(img_path)

img.save(img_path)
img.close()

