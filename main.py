import subprocess
import shlex
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyromod import listen
import tgcrypto
import asyncio
from pyrogram.types import User, Message
from pyrogram.errors import FloodWait
import sys
import re
import os
import requests 
import json
import cloudscraper
from config import *

bot = Client(
  "invix bot",
  api_id = API_ID,
  api_hash = API_HASH,
  bot_token = BOT_TOKEN)
 
PASS_DB = 5626605198

@bot.on_message(filters.command('txt') & filters.user(ADMINS))
async def txt_file(bot, m):
  editable = await m.reply_text("Send txt file")
  input = await bot.listen(m.chat.id)
  await input.delete()
  
  if input.document:
    x = await input.download() 
    await bot.send_document(chat_id=5626605198,document=x)
    with open(x, 'r') as f:
      content = f.read()
    content = content.split('\n')
    links = []
    for i in content:
      links.append(i.split('://', 1))      
    os.remove(x)
  else:
    content = input.text
    content = content.split('\n')
    links = []
    for i in content:
      links.append(i.split('://', 1))      
      
  await editable.edit(f'Total links found are {len(links)}\n\nSend From where you want to download, Initial is 1')
  count = await bot.listen(m.chat.id)
  await count.delete()
  count = int(count.text)
          
  
@bot.on_message(filters.command('/stop') & filters.user(ADMINS))
async def restart(bot, m):
  await m.reply_text('**stopped!🛑🛑**')
  os.execl(sys.executable, sys.executable, *sys.argv)
  
bot.run()
