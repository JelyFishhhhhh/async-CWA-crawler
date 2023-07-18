from time import time
from modules import Json
from gen_config import generator

from aiofiles import open as aopen
from asyncio import run
from requests import post, get
from datetime import datetime

from os import makedirs
from os.path import isdir, isfile

async def get_info():

    CONFIG = Json.load_nowait("config.json")    
    
    async with aopen("api", mode="r+", encoding="utf-8") as API:
        async for rq in API:
            
            url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/{rq[:-1]}?Authorization=" + CONFIG["TOKEN"]
            res = get(url).json()
            time = datetime.now().strftime("%Y%m%d")
            f_name = f"results/{time}_{rq[:-1]}.json"
            async with aopen(f_name, mode="w") as _:

                await Json.dump(file=f_name, data=res)

    return

if __name__ == "__main__":

    if not isfile("config.json"):
        
        generator()

    if not isdir("results"):

        makedirs("results")
    
    # start = time()
    run(get_info())
    