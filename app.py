from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/player')
def player():
    f = open("test player.html", "r")
    apphtmlp = f.read()
    f.close()
    return apphtmlp

@app.route('/window')
def window():
    f = open("test player window.html", "r")
    apphtmlw = f.read()
    f.close()
    return apphtmlw

@app.route('/controller')
def controller():
    f = open("test controller.html", "r")
    apphtmlc = f.read()
    f.close()
    return apphtmlc
