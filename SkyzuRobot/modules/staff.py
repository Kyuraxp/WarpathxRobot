from html import escape
from pyrogram import Client, filters
from pyrogram.types import Message
from SkyzuRobot import pbot


@pbot.on_message(filters.command(["p", "r"]) & filters.group)
async def pantek(client: Client, message: Message):
    rep = message.reply_to_message
    teks = message.reply_to_message.text
    chid = message.chat.id
    if teks:
        return await client.send_message(chid, teks)
    kntl = await client.download_media(rep)
    if rep.photo:
        return await client.send_photo(chid, photo=kntl)
    if rep.video:
        return await client.send_video(chid, video=kntl)
    if rep.sticker:
        return await client.send_sticker(chid, sticker=kntl)
    if rep.audio:
        judulnya = rep.audio.title
        durasinya = rep.audio.duration
        return await client.send_audio(chid, audio=kntl, duration=durasinya, title=judulnya, caption=f"**{judulnya}**")
    if rep.voice:
        return await client.send_voice(chid, voice=kntl)
    if rep.video:
        return await client.send_video(chid, video=kntl)
    if rep.document:
        return await client.send_document(chid, document=kntl)
    else:
        return


@pbot.on_message(filters.command(["staff", "admins", "adminlist"]) & ~filters.group & ~filters.bot & ~filters.edited)
def staff(client: Client, message: Message):
    creator = []
    co_founder = []
    admin = []
    admin_check = pbot.get_chat_members(message.chat.id, filter="administrators")
    for x in admin_check:
        # Ini buat nyari co-founder
        if x.status == "administrator" and x.can_promote_members and x.title:
            title = escape(x.title)
            co_founder.append(
                f" <b>├</b> <a href='tg://user?id={x.user.id}'>{x.user.first_name}</a> »<i> {title}</i>"
            )
        elif x.status == "administrator" and x.can_promote_members and not x.title:
            co_founder.append(
                f" <b>├</b> <a href='tg://user?id={x.user.id}'>{x.user.first_name}</a>"
            )
        # ini buat nyari admin
        elif x.status == "administrator" and not x.can_promote_members and x.title:
            title = escape(x.title)
            admin.append(
                f" <b>├</b> <a href='tg://user?id={x.user.id}'>{x.user.first_name}</a> »<i> {title}</i>"
            )
        elif x.status == "administrator" and not x.can_promote_members and not x.title:
            admin.append(
                f" <b>├</b> <a href='tg://user?id={x.user.id}'>{x.user.first_name}</a>"
            )
        # ini buat nyari creator
        elif x.status == "creator" and x.title:
            title = escape(x.title)
            creator.append(
                f" <b>└ ⁫</b> <a href='tg://user?id={x.user.id}'>{x.user.first_name}</a> »<i> {title}</i>"
            )
        elif x.status == "creator" and not x.title:
            creator.append(
                f" <b>└ ⁫</b> <a href='tg://user?id={x.user.id}'>{x.user.first_name}</a>"
            )

    if len(co_founder) == 0 and len(admin) == 0:
        result = f"<b>Staff {message.chat.title}</b>\n\n⚜️ <b>Founder</b>\n" + "\n".join(creator)
    elif len(co_founder) == 0 and len(admin) > 0:
        res_admin = admin[-1].replace("├", "└ ⁫")
        admin.pop(-1)
        admin.append(res_admin)
        result = f"<b>Staff {message.chat.title}</b>\n\n⚜️ <b>Founder</b>\n" + "\n".join(
            creator
        ) + "\n\n🔰‚ <b>Admin</b>\n" + "\n".join(admin)
    elif len(co_founder) > 0 and len(admin) == 0:
        resco_founder = co_founder[-1].replace("├", "└ ⁫")
        co_founder.pop(-1)
        co_founder.append(resco_founder)
        result = f"<b>Staff {message.chat.title}</b>\n\n⚜️ <b>Founder</b>\n" + "\n".join(
            creator
        ) + "\n\n🔱 <b>Co-Founder</b>\n" + "\n".join(co_founder)
    else:
        resco_founder = co_founder[-1].replace("├", "└ ⁫")
        res_admin = admin[-1].replace("├", "└ ⁫")
        co_founder.pop(-1)
        admin.pop(-1)
        co_founder.append(resco_founder)
        admin.append(res_admin)
        result = (
                f"<b>Staff {message.chat.title}</b>\n\n⚜️ <b>Founder</b>\n" + "\n".join(creator) + "\n\n"
                                                                    "🔱 <b>Co-Founder</b>\n" + "\n".join(
            co_founder) + "\n\n"
                          "🔰‚ <b>Admin</b>\n" + "\n".join(admin)
        )
    pbot.send_message(message.chat.id, result)
