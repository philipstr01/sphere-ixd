#!/bin/bash
echo getting repo
cd /home/pi/Documents/sphere-ixd
git reset --hard
git pull origin main

echo waiting 10s
sleep 10
echo executing python main
cd /home/pi/Documents/sphere-ixd/raspy/
python3 main.py &
