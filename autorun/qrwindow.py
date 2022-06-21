import json
import os
import socket
import subprocess
import threading
import qrcode
import urllib.parse
import tkinter
from tkinter import *

globalconfig = {"ip": socket.gethostbyname(socket.gethostname()), "port": 5000}

TKroot = tkinter.Tk()
qrtextjson = json.dumps(globalconfig)


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
    stream = os.popen(
        "cd C:\\Users\\jurko\Desktop\\remote-av-Player\\autorun && py test.py")
    temp = json.loads(stream.read())
    print(temp)
    x = threading.Thread(target=tkdestroy, args=(), daemon=True)
    x.start()
    print("after destroy")
    if temp["type"] == "chrome":
        print("in chrome")
        stream = os.popen(
            "cd C:\\Users\\jurko\Desktop\\remote-av-Player && py test.py")
        print("after popen")
        i = 1
        while i < 6:
            print("in while")
            streamtemp = stream.read()
            print(streamtemp)
            print("breaking")
            break
    if temp["type"] == "cmd":
        stream = os.popen(
            "cd C:\\Users\\jurko\Desktop\\remote-av-Player && " + temp["cmd"])
        stream.read()


print("before while")

x = threading.Thread(target=wsrun)

qrgenerate()
x.start()
qrshow()

contoend = False
while contoend == False:
    print("before thread")
    x.start()
    x.join()
