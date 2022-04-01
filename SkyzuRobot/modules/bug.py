# Copyright (c) 2022 Shiinobu Project

from datetime import datetime

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
)

from SkyzuRobot import pbot as Client
from SkyzuRobot import (
    OWNER_ID as owner,
    SUPPORT_CHAT as log,
)
from SkyzuRobot.utils.errors import capture_err


def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@Client.on_message(filters.command("bug"))
@capture_err
async def bug(_, msg: Message):
    if msg.chat.username:
        chat_username = (f"@{msg.chat.username} / `{msg.chat.id}`")
    else:
        chat_username = (f"Private Group / `{msg.chat.id}`")

    bugs = content(msg)
    user_id = msg.from_user.id
    mention = "["+msg.from_user.first_name+"](tg://user?id="+str(msg.from_user.id)+")"
    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)

    thumb = "https://telegra.ph/file/2bec228f120213c68a0b0.jpg"
    
    bug_report = f"""
**#BUG : ** **@Kyuraxx**
**Dari Pengguna : ** **{mention}**
**Id Pengguna : ** **{user_id}**
**Grup : ** **{chat_username}**
**Laporan Bug : ** **{bugs}**
**Waktu Laporan : ** **{datetimes}**"""
    
    if msg.chat.type == "private":
        await msg.reply_text("❎ <b>This command only works in groups.</b>")
        return

    if user_id == owner:
        if bugs:
            await msg.reply_text(
                f"❎ <b>Bagaimana pemilik bot melaporkan bug idiot??</b>",
            )
            return
        else:
            await msg.reply_text(
                f"❎ <b>Pemilik Bodoh</b>",
            )
    elif user_id != owner:
        if bugs:
            await msg.reply_text(
                f"<b>Laporan bug : {bugs}</b>\n\n"
                "✅ <b>Bug berhasil dilaporkan ke grup pendukung!</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "Tutup", callback_data=f"close_reply")
                        ]
                    ]
                )
            )
            await Client.send_photo(
                log,
                photo=thumb,
                caption=f"{bug_report}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "➡ Lihat Laporan", url=f"{msg.link}")
                        ],
                        [
                            InlineKeyboardButton(
                                "Tutup", callback_data=f"close_send_photo")
                        ]
                    ]
                )
            )
        else:
            await msg.reply_text(
                f"❎ <b>Tidak ada bug dilaporkan!</b>",
            )
        
    

@Client.on_callback_query(filters.regex("close_reply"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()

@Client.on_callback_query(filters.regex("close_send_photo"))
async def close_send_photo(Client, CallbackQuery):
    await CallbackQuery.message.delete()


_mod_name_ = "Bug"
