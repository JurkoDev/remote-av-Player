#!/usr/bin/env python
import asyncio
import pathlib
import ssl
import threading
from time import sleep
import websockets
import os
import sys
import webbrowser
import tkinter
import socket
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

global driver

# "windows","linux","mac"
normal_chrome_os = "windows"


def paired(url, opener):
    """open chrome and interact"""
    match opener:
        case "webdriver_player":
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            sleep(1)
            fullscreen_button = driver.find_element(by=By.ID, value="fullscreen")
            fullscreen_button.click()
        case "webdriver_zoom":
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            sleep(5)
            driver.quit()
        case "windows":
            # Windows
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            # Linux
            # chrome_path = '/usr/bin/google-chrome %s'
            # MacOS
            # chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            webbrowser.get(chrome_path).open(url, new=1)
        case "linux":
            # Windows
            # chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            # Linux
            chrome_path = '/usr/bin/google-chrome %s'
            # MacOS
            # chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            webbrowser.get(chrome_path).open(url, new=1)
        case "mac":
            # Windows
            # chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            # Linux
            # chrome_path = '/usr/bin/google-chrome %s'
            # MacOS
            chrome_path = 'open -a /Applications/Google/ Chrome.app %s'
            webbrowser.get(chrome_path).open(url, new=1)


async def ws_recive(websocket):
    """on websocket recive funcion"""
    async for message in websocket:
        temp = json.loads(message)
        if temp["command"] == "autorun_pair":
            await websocket.send(json.dumps({"command": "autorun_continue"}))
        if temp["command"] == "autorun_continue_response":
            print(message)
            if temp["type"] == "cmd":
                stream = os.popen(
                    "cd C:\\Users\\jurko\\Desktop\\remote-av-Player && " + temp["cmd"])
                stream.read()
            if temp["type"] == "chrome":
                exit()
            if temp["type"] == "zoom":
                paired(temp["zoom_link"],"webdriver_zoom")
                exit()


async def main():
    """main function"""
    async with websockets.serve(ws_recive, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
# paired("http://127.0.0.1:5000/player.html")
