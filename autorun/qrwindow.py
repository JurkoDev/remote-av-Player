import json
import os
import platform
import socket
import subprocess
import threading
from time import sleep
import qrcode
import urllib.parse
import requests
import tkinter
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

# netifaces.ifaddresses("{CE05DBF0-03B2-40F0-8913-8EDFE9B5327C}")[2][0]["addr"]

globalconfig = {"ip": socket.gethostbyname(socket.gethostname()), "port": 5000}

TKroot = tkinter.Tk()
qrtextjson = json.dumps(globalconfig)

whiletemp = False
while whiletemp == False:
    if globalconfig["ip"] == "127.0.0.1":
        sleep(10)
        globalconfig = {"ip": socket.gethostbyname(socket.gethostname()), "port": 5000}
    else:
        whiletemp = True

print("ip not 127.0.0.1")

def ping():
    """ping the local asset server"""
    whiletemp = False
    while whiletemp == False:
        try:
            r = requests.get('http://127.0.0.1:5000/')
            whiletemp = r.status_code == 200
        except:
            sleep(10)


def qrgenerate():
    """generate qrcode"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=2,
    )
    qr.add_data('https://www.youtube.com/watch?v=dQw4w9WgXcQ#' +
                urllib.parse.quote(qrtextjson))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrtemp.png")


def qrshow():
    """show window and qrcode"""
    TKroot.attributes("-fullscreen", True)
    debugtext = tkinter.StringVar()
    debugtext.set(qrtextjson)
    image = tkinter.PhotoImage(file="qrtemp.png")
    qrimage = tkinter.Label(TKroot, image=image)
    qrimage.pack()
    label = tkinter.Label(TKroot, textvariable=debugtext)
    label.pack()
    TKroot.mainloop()


def tkdestroy():
    """destory window"""
    TKroot.destroy()


def paired(url, opener):
    """open chrome and interact"""
    match opener:
        case "webdriver_player":
            driver.get(url)
            sleep(1)
            fullscreen_button = driver.find_element(by=By.ID, value="fullscreen")
            fullscreen_button.click()
        case "webdriver_zoom":
            driver.get(url)
            sleep(5)
            driver.quit()

def wsrun():
    """run the wslisener"""
    x = threading.Thread(target=tkdestroy, args=(), daemon=True)
    stream = os.popen(
        "cd C:\\Users\\jurko\\Desktop\\remote-av-Player\\autorun && py test.py")
    temp = json.loads(stream.read())
    print(temp)
    x.start()
    if temp["type"] == "chrome":
        paired("http://127.0.0.1:5000/player.html","webdriver_player")
        print("browser done")
        stream = os.popen(
            "cd C:\\Users\\jurko\\Desktop\\remote-av-Player && py test.py")
        print("ws done")
        i = 1
        while i == 1:
            print("in while loop")
            streamtemp = stream.read()
            print("ws read")
            print(streamtemp)
            i = 2
    if temp["type"] == "zoom":
        paired("http://127.0.0.1:5000/player.html","webdriver_player")
        stream = os.popen(
            "cd C:\\Users\\jurkov\\Desktop\\remote-av-Player && py test.py")
        i = 1
        while i == 1:
            streamtemp = stream.read()
            print(streamtemp)
            i = 2
    if temp["type"] == "cmd":
        stream = os.popen(
            "cd C:\\Users\\jurko\\Desktop\\remote-av-Player && " + temp["cmd"])
        stream.read()


ping()


x = threading.Thread(target=wsrun)

qrgenerate()
sleep(1)
x.start()
qrshow()

print("before thread")
x.join()
