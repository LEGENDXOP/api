from typing import Optional
from telethon import TelegramClient as tg
from fastapi import FastAPI
import uuid



app = FastAPI()
#bot = tg("UltraXOp", 1621727, "31350903c528876f79527398c09660ce")

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/pro/")
async def create_item(item=True):
  res = {
     "method": "post",
     "response": str(uuid.uuid4())
  }
  return res
