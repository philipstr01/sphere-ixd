#!/bin/bash
cd /home/pi/Documents/sphere-ixd
git reset --hard
git pull origin main

cd /raspy/
python3 main.py &
