from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/player')
def player():
    f = open("test player.html", "r")
    apphtmlp = f.read()
    f.close()
    return apphtmlp

@app.route('/')
def window():
    return "goto /controller or /player"

@app.route('/controller')
def controller():
    f = open("test controller.html", "r")
    apphtmlc = f.read()
    f.close()
    return apphtmlc
