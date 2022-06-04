import asyncio
import aiohttp
import time
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)

async def download(n):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://reqres.in/api/users?page{n}') as response:
            data = await response.read()
            print(c[n] + f"{data}"+c[0])

async def main():
    obj1 = download(1)
    obj2 = download(2)
    obj3 = download(3)

    # See that the three object would execute synchronously,
    # so it will take max(1, 2, 3) seconds to execute.
    start = time.time()

    await asyncio.gather(obj1, obj2, obj3)

    time_taken = time.time() - start
    print('Time Taken {0}'.format(time_taken))
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())