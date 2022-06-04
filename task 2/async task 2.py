import asyncio
import aiohttp
import aiofiles
import json
import os
import time
async def downloadjson(comic_id):
    url = f"https://xkcd.com/{comic_id}/info.0.json"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data_json = await response.json() 
            json_object = json.dumps(data_json)
            filepath = os.path.join(os.path.dirname(__file__), f"New folder2\comic_{comic_id}.json")
            async with aiofiles.open(filepath, mode='w') as f:
                await f.write(json_object)
            

async def main():
    mypath = os.path.join(os.path.dirname(__file__), f"New folder2")
    if not os.path.isdir(mypath):
        os.makedirs(mypath)
    lst = list(range(1,201))
    start = time.time()
    await asyncio.gather(*(downloadjson(n) for n in lst))
    time_taken = time.time() - start
    print('Time Taken {0}'.format(time_taken))
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())