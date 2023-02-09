#!/bin/bash
echo getting repo
cd /home/pi/Documents/sphere-ixd
git reset --hard
git pull origin main

echo executing python main
cd /home/pi/Documents/sphere-ixd/raspy/
sudo python3 main.py &
