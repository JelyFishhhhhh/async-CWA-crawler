from modules import Json

from aiofiles import open as aopen
from asyncio import run
from requests import post, get
from datetime import datetime

from os import makedirs
from os.path import isdir

CONFIG = Json.load_nowait("config.json")
async def get_info():
    
    async with aopen("api", mode="r+", encoding="utf-8") as API:
        async for rq in API:
            
            url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/{rq[:-1]}?Authorization=" + CONFIG["TOKEN"]
            res = get(url).json()
            time = datetime.now().strftime("%Y%m%d")
            f_name = f"results/{time}_{rq[:-1]}.json"
            with open(f_name, mode="w") as _:
                Json.dump_nowait(file=f_name, data=res)
                break

if __name__ == "__main__":
    if not isdir("results"):
        makedirs("results")
    run(get_info())