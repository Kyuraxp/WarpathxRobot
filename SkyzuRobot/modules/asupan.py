# ⚠️ © @kyuraxx
# ⚠️ Don't Remove Credits

import os
import random
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterVideo
from SkyzuRobot.events import register
from SkyzuRobot import telethn as tbot, ubot2                 


@register(pattern="^/asupan ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Video Asupan...🔍**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@asupankyura", filter=InputMessagesFilterVideo
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Asupan Buat Kamu 🤤", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya Jelek Semua")  


@register(pattern="^/ayang ?(.*)")
async def _(event):
    bubur = await event.reply("**Mencari Ayang...🔍**") 
    try:
        ayangnya = [
            ayang
            async for ayang in ubot2.iter_messages(
            "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        termos = random.choice(ayangnya)
        kompor = await ubot2.download_media(termos)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Ayang Nya Kamu 😬😚", 
            file=kompor
            )
        await bubur.delete()
    except Exception:
        await bubur.edit("Ayangnya Hilang Karena Anda Ga GoodLooking")  

        
@register(pattern="^/cp ?(.*)")
async def _(event):
    liong = await event.reply("**Mencari PP Couple...🔍**") 
    try:
        couplenya = [
            couple
            async for couple in ubot2.iter_messages(
            "@cpxkyura", filter=InputMessagesFilterPhotos
            )
        ]
        kopi = random.choice(couplenya)
        roko = await ubot2.download_media(kopi)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Kak PP Couplenya 😁", 
            file=roko
            )
        await liong.delete()
    except Exception:
        await liong.edit("PP Couple Nya Gaada Yang Bagus _-")  
        

__mod_name__ = "Asupan"

        
