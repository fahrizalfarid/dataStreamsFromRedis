
import asyncio
import websockets

from json import dumps,loads
from constructors.contstructor import queue


async def lidar(websocket, path):
    data = queue()
    while True:
        await websocket.send(str(data.popQueue()))
        await asyncio.sleep(1)


start_server = websockets.serve(lidar, "127.0.0.1", 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()