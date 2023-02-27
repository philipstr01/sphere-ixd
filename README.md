# sphere-ixd

**A tool to improve teanwork**

## Table of Content:
- [Description](https://github.com/philipstr01/sphere-ixd#description)
- [Installation](https://github.com/philipstr01/sphere-ixd#installation)
- [Usage](https://github.com/philipstr01/sphere-ixd#usage)
- [Acknowledgements](https://github.com/philipstr01/sphere-ixd#acknowledgements)
- [License](https://github.com/philipstr01/sphere-ixd#license)
## Description

## Installation
### The Raspberry Pi
We use Raspberry Pi OS (32-bit) 2022-09-22 on a Raspberry Pi 4 Model B.
The OS can be installed via the [Raspberry Pi imager](https://www.raspberrypi.com/software/). Notice that our configuration was headless,
meaning that we had to enable SSH and configure a WiFi connection inside the imager. 

As depicted  here:

![imagersettings](https://user-images.githubusercontent.com/85298560/214868522-06e33cfc-d6da-4eb2-95f9-11187529c631.png)

You need to install python 3 and the following pip packages:
```
sudo pip install pandas
sudo pip install limepy
sudo pip install GitPython
sudo pip install rpi_ws281x 
sudo pip install adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
```


Once you have set up the Pi, you can place the whole repo in the Documents folder so that its path will be **/home/pi/Documents/sphere-ixd**.

When you want to start your programm just execute **startup.sh**.

### The Limesurvey Website

## Usage

Once everything has been setup, the sphere is ready to use. Sphere will be, by default, in a resting state. Once answers are submitted to your LimeSurvey site, Sphere will wake up and start displaying the summarized results.

| Rest State  | Activated |
| ------------- | ------------- |
| <img src="https://user-images.githubusercontent.com/85298560/221534627-588d891e-c352-465a-9959-7b2fe91bef11.jpeg" width=70% height=70%>  | <img src="https://user-images.githubusercontent.com/85298560/221534742-ba6b5d19-16c6-4836-91e9-9121a5e6da8b.jpeg" width=50% height=50%>  |

After half an hour, the sphere will reset to its resting state, after which answers can be displayed again.

For easy use of the artifact, we recommend placing a QR-code of your survey website near Sphere.

<img src="https://user-images.githubusercontent.com/85298560/221582088-9d64920c-271c-4fa3-9590-c8ac8de20210.jpeg" width=50% height=50%>

## Acknowledgements
## License


