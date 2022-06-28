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
from tkinter import *

globalconfig = {"ip": socket.gethostbyname(socket.gethostname()), "port": 5000}

TKroot = tkinter.Tk()
qrtextjson = json.dumps(globalconfig)


def ping():
    whiletemp = False
    while whiletemp == False:
        try:
            r = requests.get('http://127.0.0.1:5000/')
            whiletemp = r.status_code == 200
        except:
            sleep(10)    


def qrgenerate():
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
    TKroot.attributes("-fullscreen", True)
    debugtext = StringVar()
    debugtext.set(qrtextjson)
    image = PhotoImage(file="qrtemp.png")
    qrimage = Label(TKroot, image=image)
    qrimage.pack()
    label = Label(TKroot, textvariable=debugtext)
    label.pack()
    TKroot.mainloop()


def tkdestroy():
    TKroot.destroy()


def wsrun():
    x = threading.Thread(target=tkdestroy, args=(), daemon=True)
    wsrunwhile = False
    while wsrunwhile == False:
        stream = os.popen(
            "cd C:\\Users\\jurko\Desktop\\remote-av-Player\\autorun && py test.py")
        temp = json.loads(stream.read())
        print(temp)
        x = threading.Thread(target=tkdestroy, args=(), daemon=True)
        x.start()
        if temp["type"] == "chrome":
            stream = os.popen(
                "cd C:\\Users\\jurko\Desktop\\remote-av-Player && py test.py")
            i = 1
            while i == 1:
                streamtemp = stream.read()
                print(streamtemp)
                i = 2
        if temp["type"] == "zoom":
            stream = os.popen(
                "cd C:\\Users\\jurko\Desktop\\remote-av-Player && py test.py")
            i = 1
            while i == 1:
                streamtemp = stream.read()
                print(streamtemp)
                i = 2
        if temp["type"] == "cmd":
            stream = os.popen(
                "cd C:\\Users\\jurko\Desktop\\remote-av-Player && " + temp["cmd"])
            stream.read()


ping()


x = threading.Thread(target=wsrun)

qrgenerate()
x.start()
qrshow()

contoend = False
while contoend == False:
    print("before thread")
    x.start()
    x.join()
