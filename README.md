# remote-av-Player
a remote controller and player combo in html
funguje na chrome v pocitaci a na androide

web server setup
v konzole v priecinku s tymto kodom
windows:
> py -3 -m venv venv

> venv\Scripts\activate

> pip install Flask

> flask run --host=0.0.0.0

linux:
> python3 -m venv venv

> . venv/bin/activate

> pip install Flask

> flask run --host=0.0.0.0

ws server setup
windows + linux:
> pip install websockets

> python test.py



start:

web server start
v konzole v priecinku s tymto kodom

skratka pre linux v rpi:
> sh /home/pi/Desktop/remote-av-Player/flask.sh

> sh /home/pi/Desktop/remote-av-Player/ws.sh

windows:
> venv\Scripts\activate

> flask run --host=0.0.0.0

linux:
> . venv/bin/activate

> flask run --host=0.0.0.0

ws server start
windows + linux:
> python test.py

contoller
> http://serverip:5000/controller

player
> http://serverip:5000/player



conroller controls:
![image](https://user-images.githubusercontent.com/50539591/166234683-f752109b-a738-456d-998a-f3a2b508618d.png)


player setup:
![image](https://user-images.githubusercontent.com/50539591/166239035-ec5e5b6a-51b5-4536-b7f4-035649b26dac.png)
