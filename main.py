from typing import Optional
from telethon import TelegramClient as tg
from fastapi import FastAPI

app = FastAPI()
bot = tg("UltraXOp", 1621727, "31350903c528876f79527398c09660ce")

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
	  if q == None:
	    return {"chat": item_id, "message": "not found message"}
	  await bot.start()
	  await bot.send_message(item_id, q)
	  return {"chat": item_id, "message": q}

@app.post("/pro/")
async def create_item(item=True):
  res = {
    	"method": "post",
    	"response": item
  }
  return res
