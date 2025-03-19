#!/usr/bin/env bash

cd "$(dirname "$0")"

source .venv/bin/activate
python himawari.py

# hyprctl hyprpaper reload ,contain:`pwd`/lastest.png
hyprctl hyprpaper reload ,`pwd`/lastest.png

