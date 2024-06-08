import asyncio
import time

from wrap import *


async def run():
    startup_event()
    while True:
        for i in range(0, 30, 1):
            await send_level(i)
            time.sleep(2)
        for i in range(30, 0, -1):
            await send_level(i)
            time.sleep(2)

def main():
    asyncio.run(run())


main()