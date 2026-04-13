#!/usr/bin/env bash

cd "$(dirname "$0")"

# source .venv/bin/activate
uv run himawari.py

prev_swaybg=`pgrep -x swaybg`

swaybg -i `pwd`/lastest.png -m fill &
echo "Started swaybg with PID: $!"

sleep 1

if [ -n "$prev_swaybg" ]; then
    echo "Killing previous swaybg process with PID: $prev_swaybg"
    kill $prev_swaybg
fi

