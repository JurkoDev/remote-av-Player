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

async def main():
    async with websockets.serve(echo, "0.0.0.0" , 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())