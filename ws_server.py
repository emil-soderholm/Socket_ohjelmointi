# websockets server
import asyncio
import datetime
import random
import websockets

async def myServ(ws, path):
    while True:
        now = 'VAMK' + datetime.datetime.now().isoformat()
        await ws.send(now)
        await asyncio.sleep(1 + random.random()*3)

# create ws server
start_server = websockets.serve(myServ, '0.0.0.0', 11111)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()