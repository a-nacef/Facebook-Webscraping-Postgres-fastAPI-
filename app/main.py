from fastapi import FastAPI, testclient
from scrape import Scraper


app = FastAPI()
s = Scraper()


@app.get("/")
async def livecheck():
    return "Hello from the webscraper!"

#Raw posts data with every key
@app.get("/raw/{num}")
async def get_data(num: int):
    return s.getdata(num)


#Pruned data with just the post_id and the corresponding text
@app.get("/text/{num}")
async def get_data(num:int):
    resp = s.getdata(num)
    return {x["post_id"]:x["text"] for x in resp}



