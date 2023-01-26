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
We use Raspberry Pi OS (32-bit) 2022-09-22 on a Raspberry Pi 4 Model B.
The OS can be installed via the [Raspberry Pi imager](https://www.raspberrypi.com/software/). Notice that our configuration was headless,
meaning that we had to enable SSH and configure a WiFi connection inside the imager. 

As depicted  here:

![imagersettings](https://user-images.githubusercontent.com/85298560/214868522-06e33cfc-d6da-4eb2-95f9-11187529c631.png)

You need to install python 3 and the following pip packages:
- pandas
- limepy
- GitPython

Once you have set up the Pi, you can place the whole repo in the Documents folder so that its path will be **/home/pi/Documents/sphere-ixd**.
Afterwards, [edit the **rc.local** file](https://raspberrypi-guide.github.io/programming/run-script-on-boot) and add the path **/home/pi/Documents/shpere-ixd/startup.py**. 

When the Raspberry Pi is powered on, it should now automatically update the program files and run the program. 

## Usage
## Acknowledgements
## License


