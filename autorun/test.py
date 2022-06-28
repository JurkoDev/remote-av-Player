#!/usr/bin/env python
from asyncio import *
import asyncio
import pathlib
import ssl
import threading
import websockets
import os
import sys
from os import *
import webbrowser
from tkinter import *
import socket
import json


def paired(url):
    # Windows
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    # Linux
    # chrome_path = '/usr/bin/google-chrome %s'
    # MacOS
    # chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    webbrowser.get(chrome_path).open(url)


async def echo(websocket):
    async for message in websocket:
        temp = json.loads(message)
        if temp["command"] == "autorun_pair":
            await websocket.send(json.dumps({"command": "autorun_continue"}))
        if temp["command"] == "autorun_continue_response":
            print(message)
            if temp["type"] == "cmd":
                stream = os.popen(
                    "cd C:\\Users\\jurko\Desktop\\remote-av-Player && " + temp["cmd"])
                stream.read()
            if temp["type"] == "chrome":
                paired("http://127.0.0.1:5000/player.html")
                exit()
            if temp["type"] == "zoom":
                paired(temp["zoom_link"])
                paired("http://127.0.0.1:5000/player.html")
                exit()


async def main():
    async with websockets.serve(echo, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
# paired()
