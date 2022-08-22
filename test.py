#!/usr/bin/env python
import os
import asyncio
# import pathlib
# import ssl
import websockets
import json

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
# ssl_context.load_cert_chain(localhost_pem)

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
        stream = os.popen('cd C:\\Users\\jurko\\Desktop\\firebase\\public && youtube-dl --no-call-home --sub-format vtt --sub-lang sk --write-auto-sub -o "%(id)s.%(ext)s" ' + link)
        # stream = os.popen('cd C:\\Users\\jurko\\Desktop\\firebase\\public && youtube-dl --no-call-home -o "%(id)s.%(ext)s" ' + link)
        streamtemp = stream.read()
        print("dowload done")
        stream = os.popen('youtube-dl --no-call-home --get-filename -o "%(id)s.mkv" ' + link)
        streamtemp = stream.read()
        stream2 = os.popen('youtube-dl --no-call-home --get-filename -o "%(id)s.sk.vtt" ' + link)
        streamtemp2 = stream2.read()
        jsontemp = json.loads('{"command":"media_youtube_video_offline","url":""}')
        jsontemp["url"] = "http://127.0.0.1:5000/" + streamtemp
        jsontemp["subs"] = "http://127.0.0.1:5000/" + streamtemp2
        websockets.broadcast(CLIENTS, json.dumps(jsontemp))
    if temp["command"] == "media_play_youtube":
        link = temp["link"]
        stream = os.popen("youtube-dl --no-call-home -f 136 -g " + link)
        streamtemp = stream.read()
        if streamtemp in "ERROR: requested format not available":
            stream = os.popen("youtube-dl --no-call-home -f 135 -g " + link)
            streamtemp = stream.read()
        jsontemp = json.loads('{"command":"media_play_youtube_video","link":""}')
        jsontemp["link"] = streamtemp
        websockets.broadcast(CLIENTS, json.dumps(jsontemp))
        stream = os.popen("youtube-dl --no-call-home -f 140 -g " + link)
        streamtemp = stream.read()
        jsontemp = json.loads('{"command":"media_play_youtube_audio","link":""}')
        jsontemp["link"] = streamtemp
        websockets.broadcast(CLIENTS, json.dumps(jsontemp))
    if temp["command"] == "media_play_youtube_name":
        link = temp["link"]
        stream = os.popen("youtube-dl --no-call-home -e " + link)
        streamtemp = stream.read()
        jsontemp = json.loads('{"command":"media_youtube_video_name","note":""}')
        jsontemp["note"] = streamtemp
        websockets.broadcast(CLIENTS, json.dumps(jsontemp))
    if temp["command"] == "queue_load_playlist":
        link = temp["link"]
        stream = os.popen("youtube-dl --no-call-home --flat-playlist --get-id " + link)
        streamtemp = stream.read().split("\n")
        streamtemp.pop()
        jsontemp = json.loads('{"command":"queue_load_playlist_response","link_array":""}')
        jsontemp["link_array"] = streamtemp
        websockets.broadcast(CLIENTS, json.dumps(jsontemp))
    if temp["command"] == "autorun_reset":
        print("exited")
        exit()

async def main():
    async with websockets.serve(echo, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
