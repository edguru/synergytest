
"""Check if userbot awake or not . 
"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PIC = Config.ALIVE_PHOTTO
if ALIVE_PIC is None:
   ALIVE_PIC = "https://telegra.ph/file/1ab92cc6f82851b0a7106.jpg"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = Config.ALIVE_MSG
if ALIVE_MESSAGE is None:
   ALIVE_MESSAGE = "**😈☠️SYNERGY IS HERE🔥⚡\n\n\n**"
   ALIVE_MESSAGE += "`My Bot Status \n\n\n`"
   ALIVE_MESSAGE += f"`Telethon: TELETHON-15.0.0 \n\n`"
   ALIVE_MESSAGE += f"`Python: PYTHON-3.8.5 \n\n`"
   ALIVE_MESSAGE += "`I'll Serve you as long as I live. But I am immortal so with every new month I will be born again\n\n`"
   ALIVE_MESSAGE += f"`Support Channel` : @synergyOT \n\n"
   ALIVE_MESSAGE += f"`MY BOSS🤗`: {DEFAULTUSER} \n\n "
                
            
#@command(outgoing=True, pattern="^.summon$")
@borg.on(admin_cmd(pattern=r"summon"))
async def amireallyalive(summon):
    """ For .summon command, check if the bot is running.  """
    await summon.delete() 
    await borg.send_file(summon.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)
