import aiohttp
import time
import asyncio

from src.config import WS_URL


async def main():
    async with aiohttp.ClientSession() as session:
        client_id = int(time.time() * 1000)
        async with session.ws_connect(f'http://{WS_URL}/chat/ws/{client_id}') as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    with open("ws_messages.txt", "a") as file:
                        file.write(f"{msg.data}\n")

asyncio.run(main())
