from pyrogram import Client, filters
import requests
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VIPMUSIC import pbot as app

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"f"https://t.me/{app.username}?startgroup=true"),
    ],
]

# URL for the Bored API
bored_api_url = "https://apis.scrimba.com/bored/api/activity"


# Function to handle /bored command
@app.on_message(filters.command("bored", prefixes="/"))
async def bored_command(client, message):
    # Fetch a random activity from the Bored API
    response = requests.get(bored_api_url)
    if response.status_code == 200:
        data = response.json()
        activity = data.get("activity")
        if activity:
            # Send the activity to the user who triggered the command
            await message.reply(f"❖ ғᴇᴇʟɪɴɢ ʙᴏʀᴇᴅ ? ʜᴏᴡ ᴀʙᴏᴜᴛ ⏤͟͟͞͞★\n\n❅ `{activity}`\n\n❖ ғᴇᴇʟɪɴɢ ʙʏ ➥ [αиσиумσυѕ χ мυѕι¢](htps://t.me/jooxstream)", reply_markup=InlineKeyboardMarkup(EVAA),)
        else:
            await message.reply("⬤ ɴᴏ ᴀᴄᴛɪᴠɪᴛʏ ғᴏᴜɴᴅ.")
    else:
        await message.reply("⬤ ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴀᴄᴛɪᴠɪᴛʏ.")


__HELP__ = """

⬤ /bored * ➥* ɢᴇᴛ ʀᴀɴᴅᴏᴍ ʙᴏʀᴇᴅ ғᴇᴇʟɪɴɢs.
"""

__MODULE__ = "ғᴇᴇʟɪɴɢs"
