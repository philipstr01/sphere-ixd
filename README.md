# sphere-ixd

**EMOTIONAL WELLBEING AT WORK**

## Table of Content:
- [Description](https://github.com/philipstr01/sphere-ixd#description)
- [Installation](https://github.com/philipstr01/sphere-ixd#installation)
- [Usage](https://github.com/philipstr01/sphere-ixd#usage)
- [Acknowledgements](https://github.com/philipstr01/sphere-ixd#acknowledgements)
- [License](https://github.com/philipstr01/sphere-ixd#license)
## Description
### The Concept
Emotional openness is an increasingly important topic in today's workplace culture.
Employees want to be able to be open and authentic with their emotions and
thoughts.  To create a mutually respectful way of dealing with emotions, it is
It is important that we have a space where we can reflect well and share our inner life in a
safe framework.

Sphere creates such a safe framework and routines. Through regular reflection
We learn to better reflect ourselves, our thoughts, and our emotions by asking questions.
For some, this comes naturally; for others, it's a helpful exercise. Team members
answer three questions once a week directly on the Sphere website. The physical
representation of the collected and analyzed answers the object Sphere subsequently makes the overall emotional impression tangible and palpable to the team.
The team members thus gets a good impression of how the team is currently feeling and are encouraged to get in exchange about it.

Sphere focuses on the following three areas to make this possible: How is the
mood of your team? How satisfied is your team with the team dynamics? What is
your team's stress level? Sphere offers the possibility to gently integrate the
topic of emotional well-being at work into your daily work routine.

Sphere will be hung in any room at your
office. It can then be accessed individually by each
team via the website.
Via the parameters "light color" , "hanmony of the spheres" and "height of the spheres," the collected and analysed the answers of the team members are displayed.
The lower the spheres all hang, the sooner the mood
of your team is "really down." The more harmonious
or disharmonious the overall ball picture appears,
the better or worse your team dynamics look. The
Light colours range from yellow with little stress to red with much stress.


### The Prototype
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
- Hanne Wegener (Product-Design)
- [Maya Giri](https://github.com/mygiri) (Computer Science)
- [Philip Stricker](https://github.com/philipstr01) (Computer Science)

## License
MIT License

Copyright (c) 2023 Maya Giri & Philip Stricker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

