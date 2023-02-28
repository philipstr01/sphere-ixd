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
thoughts. To create a mutually respectful way of dealing with emotions, it is important that we have a space where we can reflect well and share our inner life in a
safe framework.

Sphere creates such a safe framework and routines. Through regular reflection
We learn to better reflect ourselves, our thoughts, and our emotions by asking questions.
For some, this comes naturally; for others, it's a helpful exercise. Team members
answer three questions once a week directly on the Sphere website. The physical
representation of the collected and analyzed answers the object Sphere subsequently makes the overall emotional impression tangible and palpable to the team.
The team members thus get a good impression of how the team is currently feeling and are encouraged to get in exchange about it.

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

For further information about the design concept visit: https://www.codingixd.org/lets-get-physical/ 

<img src="https://user-images.githubusercontent.com/85298560/221627110-73ba7104-3e9a-4e0b-a770-1b8dc1fce668.jpg" width=50% height=50%>

### The Prototype

For the prototype, we decided to build a cutout from the concept. We made nine individual spheres and controlled them with five small stepper motors. Stepper motors are a natural choice because they allow for precise rotations and would not turn without being powered. The spheres were connected to the motors via a string that would go through the back, where the motors were located. To control the prototype, we picked the Raspberry Pi 4 B since it has more than enough pins for the motors and can connect to the internet to download survey results. For LEDs, we went for a strip of WS2812B since they are really common and have a lot of documentation. Because we wanted a lot of light, we had to really think about our power supply. We used a phone charger to power the Pi and a 5V 5A supply to power both LEDs and motors. This would ensure that sudden fluctuations in power demand would not interrupt the voltage delivered to the Pi. We also had to use cables that could bear the load of the power supply.


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

For the limesurvey web questionnaire, we used our zedat userpage that is provided by our university. 
Follow the steps of installation of LimeSurvey on your userpage by this guide:
https://userpage.fu-berlin.de/~rober/blog/2016/02/limesurvey-install-userpage/

After completing this installation, you might still have trouble accessing the admin page for setting up your survey. Therefore, some extra tuning is necessary concerning the access rights. So, check whether the directories containing the accessed web page and the files being accessed have the correct access rights.
The directories and the web page must not be writable by groups or globally.
To adjust the rights accordingly, please log in via SSH on the computer Login.zedat.fu-berlin.de. There, you can then change the rights with the following command:
```chmod -R go-w ~/public_html/```
This command removes all write permissions (except for the owner of the data) for all files and directories within the directory ~/public_html and for the directory itself.

Now accessing the admin page should be possible and one can start setting up the survey. LimeSurvey itself is pretty self-explanatory and straightforward. 
Click create a new survey and happy tinkering! If you want to know how to access some extra style changes by CSS, do the following:
In the upper toolbar, click configuration, then themes. Create an extended version of the default themes. We used fruity and created an extend_fruity theme. In the theme editor, you can overwrite the default code in the CSS files under custom.css. 
Here, our CSS Code we used : 

```
.fruity .btn-primary {
  color: #000;
  background-color: #fff;
  border: 1px solid #000;
}

.fruity .btn-default {
  background-color: #fff;
  border: 1px solid #000;
  color: #000;
}

.fruity .btn-default:hover, .fruity .btn-default:focus, .fruity .btn-default:active, .fruity .btn-default.active, .fruity .open .dropdown-toggle.btn-default {
  color: #000;
  border: 2px solid #000;
  background-color: #fff;
}

.fruity .btn-primary:hover, .fruity .btn-primary:focus, .fruity .btn-primary:active, .fruity .btn-primary.active, .fruity .btn-primary.active:focus, .fruity .open .dropdown-toggle.btn-primary {
  color: #000;
  background-color: #fff;
  border: 2px solid #000;
}

.question-container {
  background-color: #ffffff;
  border: 1px solid #000;
  box-shadow: 0 1px 2px rgba(0,0,0,.2);
}
.fruity .text-info {
  color: #328637;
}

.font-noto {
  font-family: Trebuchet MS;
}
.fruity a {
  color: #000;
}

.fruity a:hover {
  color: #000;
}
.col-xs-6 {
  width: 50%;
}
#navigator-container > div {
  padding: 3px;
}

.fruity .navbar a{
    
    display: none;
}

.fruity .btn-primary:visited, .fruity .btn-primary:focus, .fruity .btn-primary:active, .fruity .btn-primary.active, .fruity .btn-primary.active:focus, .fruity .open .dropdown-toggle.btn-primary {
  color: #000;
  background-color: #fff;
  border: 2px solid #000;
}

.fruity .question-item {
   font-size: 20px;
  line-height: 0.85;
}
```
Our link to the survey: https://userpage.fu-berlin.de/~girim00/survey/limesurvey/index.php/419977?lang=en 

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
MIT License 2023 Maya Giri & Philip Stricker


