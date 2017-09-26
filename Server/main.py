import json
import asyncio
import websockets


async def anw(websocket):
    while True:
        try:
            q = await websocket.recv()
            question = json.loads(q)

            a = json.dumps({
                'hello': 'world!!!'
            })
            await websocket.send(a)
            print('> {}'.format(a))
        except Exception as e:
            print('Error {}'.format(e))


server = websockets.serve(anw, 'localhost', 6666)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
