#!/usr/bin/env python
import os
import asyncio
import websockets
import json

CLIENTS = set()
async def echo(websocket):
    CLIENTS.add(websocket)
    async for message in websocket:
        websockets.broadcast(CLIENTS, message)
        temp = json.loads(message)
        asyncio.create_task(youtube_dl_run(temp))

async def youtube_dl_run(temp):
    if temp["command"] == "media_youtube_offline":
        link = temp["link"]
        print("dowloading " + link)
        stream = os.popen('cd C:\\Users\\jurko\Desktop\\firebase\\public && youtube-dl --no-call-home -o "%(id)s.mp4" ' + link)
        streamtemp = stream.read()
        print("dowload done")
        stream = os.popen('youtube-dl --no-call-home --get-filename -o "%(id)s.mp4" ' + link)
        streamtemp = stream.read()
        jsontemp = json.loads('{"command":"media_youtube_video_offline","url":""}')
        jsontemp["url"] = "http://localhost:5000/" + streamtemp
        websockets.broadcast(CLIENTS, json.dumps(jsontemp))
    if temp["command"] == "media_play_youtube":
        link = temp["link"]
        stream = os.popen("youtube-dl -f 136 -g " + link + "--no-call-home")
        streamtemp = stream.read()
        jsontemp = json.loads('{"command":"media_play_youtube_video","link":""}')
        jsontemp["link"] = streamtemp
        websockets.broadcast(CLIENTS, json.dumps(jsontemp))
        stream = os.popen("youtube-dl -f 140 -g " + link + "--no-call-home")
        streamtemp = stream.read()
        jsontemp = json.loads('{"command":"media_play_youtube_audio","link":""}')
        jsontemp["link"] = streamtemp
        websockets.broadcast(CLIENTS, json.dumps(jsontemp))
    if temp["command"] == "media_play_youtube_name":
        link = temp["link"]
        stream = os.popen("youtube-dl -e " + link + "--no-call-home")
        streamtemp = stream.read()
        jsontemp = json.loads('{"command":"media_youtube_video_name","note":""}')
        jsontemp["note"] = streamtemp
        websockets.broadcast(CLIENTS, json.dumps(jsontemp))
    if temp["command"] == "autorun_reset":
        print("exited")
        exit()

async def main():
    async with websockets.serve(echo, "0.0.0.0" , 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
