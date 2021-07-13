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
async def create_bot(token):
  token = urllib.parse.unquote(token)
  print (token)
  token = dict(token)
  bot = tg(token["token"], API_ID, API_HASH)
  await bot.start(bot_token=token["token"])
  await bot.send_message("legendx22", "hello")
  await bot.log_out()
  res = {
     "method": "put",
     "response": token["token"]
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
