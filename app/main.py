from fastapi import FastAPI, testclient
import psycopg2
from scrape import Scraper
import db

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

#N-ranked data on a specific metric (Likes, comments, shares)
@app.get("/rank/{num}&metric={metric}")
async def get_ranked(num:int,metric:str):
    tup_to_json = lambda tup: {k:v for k,v in zip(s.wanted_keys,tup)}
    #Handling nonexistent metrics
    if str.lower(metric) not in ["likes", "comments", "shares"]:
        return "Incorrect metric, valid values are: likes, comments and shares"
    try:
        cur,_ = db.connect()
    except psycopg2.Error as e:
        print(f"Connection failed with error:{e}")
    cur.execute(f"SELECT * FROM posts ORDER BY {str.lower(metric)} DESC LIMIT {num}")
    query = cur.fetchall()
    if query:
        return [tup_to_json(tup) for tup in query]            
    else:
        return []
                