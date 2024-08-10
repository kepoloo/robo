import random
import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from VIPMUSIC import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID,BOT_NAME,START_IMG

MISHI = [
    "https://telegra.ph//file/2ca21769aa93db06cf773.jpg",
]

Avisha = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/roy_editx")
    ],
]



@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("🤍")
    await asyncio.sleep(0.2)
    await accha.edit("🖤")
    await asyncio.sleep(0.1)
    await accha.edit("🧡")
    await asyncio.sleep(0.1)
    await accha.edit("💚")

    await accha.delete()
    await asyncio.sleep(0.3)
    umm = await m.reply_sticker(
        "CAACAgUAAxkDAAJHbmLuy2NEfrfh6lZSohacEGrVjd5wAAIOBAACl42QVKnra4sdzC_uKQQ"
    )
    await umm.delete()
    await asyncio.sleep(0.2)
    await m.reply_photo(
        random.choice(MISHI),
        caption=f"""**❖ ʜᴇʏ, ɪ ᴀᴍ [{BOT_NAME}](f"t.me/{BOT_USERNAME}") **\n\n● **ʟɪʙʀᴀʀʏ ➥** `{lver}`\n● **ᴛᴇʟᴇᴛʜᴏɴ ➥** `{tver}`\n● **ᴘʏʀᴏɢʀᴀᴍ ➥** `{pver}`\n● **ᴘʏᴛʜᴏɴ ➥** `{pyver()}`\n\n❖ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥** [αиσиумσυѕ χ мυѕι¢](tg://user?id={OWNER_ID})""",
        reply_markup=InlineKeyboardMarkup(Avisha),
    )
    
__mod_name__ = "ᴀʟɪᴠᴇ"

__help__ = """

 ⬤ /alive ➥ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ sᴛᴀᴛᴜs.
 ⬤ /ping ➥ ᴄʜᴇᴄᴋ ᴘɪɴɢ sᴛᴀᴛᴜs.
 ⬤ /stats ➥ ᴄʜᴇᴄᴋ ʙᴏᴛ sᴛᴀᴛs.
 ⬤ /pingall ➥ ᴄʜᴇᴄᴋ ᴘɪɴɢ sᴛᴀᴛᴜs ᴏғ ᴀʟʟ ᴍᴏᴅᴜʟᴇs.
 """
    
