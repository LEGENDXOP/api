from typing import Optional
from telethon import TelegramClient as tg
from fastapi import FastAPI
import os
import uuid
from pydantic import BaseModel
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")


class Token(BaseModel):
    token: str
    username: Optional[str] = None


app = FastAPI()
#bot = tg("UltraXOp", 1621727, "31350903c528876f79527398c09660ce")

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.put("/addtoken/{token}")
async def create_bot(token):
  bot = tg(token, API_ID, API_HASH).start(bot_token=token)
  async with bot:
    await bot.send_message("legendx22", "hello")
  res = {
     "method": "post",
     "response": token
  }
  return res

@app.post("/token")
async def create_item(token):
  data = (await request.form())._dict
  res = {
     "method": "post",
     "response": data["token"]
  }
  return res
