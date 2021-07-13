from typing import Optional
from telethon import TelegramClient as tg
from fastapi import FastAPI
import os
import urllib
import uuid
from pydantic import BaseModel
API_ID = os.environ.get("APP_ID")
API_HASH = os.environ.get("API_HASH")


class Token(BaseModel):
    token: str
    username: Optional[str] = None

app = FastAPI()

class run:
  def __init__(self):
    self.pro = True
  @staticmethod
  async def start(bot):
    return await bot.get_me()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.put("/addtoken/{token}")
async def create_bot(token: str, msg: Optional[str]="hello", chatid: Optional[str]="LEGENDX22", limit: Optional [str] = "5"):
  data = {
  "token": token,
  "msg": msg,
  "chatid": chatid,
  "limit": int(limit)
  }
  bot = tg(data["token"], API_ID, API_HASH)
  await bot.start(bot_token=data["token"])
  for x in range (data["limit"])
    await bot.send_message(data["chatid"], data["msg"])
  await bot.log_out()
  res = {
     "method": "put request",
     "response": "success"
  }
  return res

from fastapi import Request


@app.post("/token")
async def create_item(request: Request):
  data = (await request.form())._dict
  res = {
     "method": "post",
     "response": data["token"],
  }
  return res
