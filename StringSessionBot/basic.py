from data import Data
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, Message, InlineKeyboardButton, CallbackQuery
from pyrogram.enums.parse_mode import ParseMode
import re, asyncio, time, shutil, psutil, os, sys, random

def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

#Kristy 

BOT_START_TIME = time.time()
currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - BOT_START_TIME))
total, used, free = shutil.disk_usage(".")
total = humanbytes(total)
used = humanbytes(used)
free = humanbytes(free)
cpu_usage = psutil.cpu_percent()
ram_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'
    
START_TEXT = """
<b> Hᴇʟʟᴏ {}

Iᴀᴍ ᴀ Tᴇʟᴇɢʀᴀᴍ Fɪʟᴇ Sᴛʀᴇᴀᴍɪɴɢ Bᴏᴛ As Wᴇʟʟ ᴀs Dɪʀᴇᴄᴛ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴏʀ

Cʟɪᴄᴋ Oɴ Hᴇʟᴘ Bᴜᴛᴛᴏɴ Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Usᴇ Mᴇʜ !!

Wᴀʀɴɪɴɢ ⚠	
Nsғᴡ Rᴇsᴛʀɪᴄᴛᴇᴅ 🚫 Bʀᴇᴀᴋɪɴɢ Rᴜʟᴇs Lᴇᴀᴅs Yᴏᴜ Tᴏ Pᴇʀᴍᴀɴᴇɴᴛ Bᴀɴ 

Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : <a href='https://t.me/Abt_Kristy'>Kʀɪsᴛʏ கிறிஸ்டி</a>
</b>
"""

HELP_TEXT = """
<b> 
➤ Sᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇ (Oʀ) Mᴇᴅɪᴀ Fʀᴏᴍ Tᴇʟᴇɢʀᴀᴍ.
➤ I Wɪʟʟ Pʀᴏᴠɪᴅᴇ Exᴛᴇʀɴᴀʟ Dɪʀᴇᴄᴛ Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ & Oɴʟɪɴᴇ Wᴀᴛᴄʜɪɴɢ Lɪɴᴋ !!
➤ Aᴅᴅ Mᴇ Iɴ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Fᴏʀ Dɪʀᴇᴄᴛ Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋs Bᴜᴛᴛᴏɴ
➤ Tʜɪs ɪs Pᴇʀᴍᴀɴᴀɴᴛ Lɪɴᴋ Uɴᴛɪʟʟ I Dᴇʟᴇᴛᴇ

Wᴀʀɴɪɴɢ ⚠	
Nsғᴡ Rᴇsᴛʀɪᴄᴛᴇᴅ 🚫 Bʀᴇᴀᴋɪɴɢ Rᴜʟᴇs Lᴇᴀᴅs Yᴏᴜ Tᴏ Pᴇʀᴍᴀɴᴇɴᴛ Bᴀɴ 

Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ (Oʀ) Rᴇᴘᴏʀᴛ Bᴜɢꜱ : <a href='https://t.me/KristyX_TG'>Kʀɪsᴛʏ கிறிஸ்டி | 🇮🇳 |</a> </b>"""

ABOUT_TEXT = """<b>
✯ Mʏ Nᴀᴍᴇ: Fɪʟᴇ Tᴏ Lɪɴᴋ/Sᴛʀᴇᴀᴍ
✯ Cʀᴇᴀᴛᴏʀ: <a href='https://t.me/Abt_Kristy'>Kʀɪsᴛʏ கிறிஸ்டி | 🇮🇳 |</a>
✯ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>
✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a>
✯ DᴀᴛᴀBᴀsᴇ: <a href='https://www.mongodb.com/'>MᴏɴɢᴏDB</a>
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href='https://heroku.com/'>Hᴇʀᴏᴋᴜ</a>
✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v2.7.2 [ KX ]</b>"""

STATS_TEXT = f"""<b><u>Bot Statistics</b></u>

• Uptime: <code>{currentTime}</code>
• CPU Usage: <code>{cpu_usage}%</code>
• RAM Usage: <code>{ram_usage}%</code>
• Total Disk Space: <code>{total}</code>
• Used Space: <code>{used} ({disk_usage}%)</code>
• Free Space: <code>{free}</code>
"""

OWNER_TEXT = """
<b>ɴᴏᴛᴇ :

⚠️Tʜɪꜱ Bᴏᴛ Iꜱ Aɴ Oᴘᴇɴ Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ

▸ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ : [ʜᴇʀᴇ](https://telegram.dog/Abt_Kristy)
▸ Iꜰ Yᴏᴜ Wᴀɴᴛ Pʀɪᴠᴀᴛᴇ Bᴏᴛ LɪᴋE Tʜɪꜱ Cᴏɴᴛᴀᴄᴛ Mᴇ..!!

▸ Dᴇᴠ : Kʀɪsᴛʏ கிறிஸ்டி | 🇮🇳 |</b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⤬ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ⤬', url=f'http://t.me/FileToLinkDL_Bot?startchannel=true')
        ],[
        InlineKeyboardButton('♚ Bᴏᴛ Oᴡɴᴇʀ', callback_data="owner_info")
        ],[
        InlineKeyboardButton('✇ Uᴘᴅᴀᴛᴇs ', url=f"https://t.me/{Var.UPDATES_CHANNEL}"),
        InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ ⌬', url=f"https://t.me/{Var.UPDATES_CHANNEL}")
        ],[
        InlineKeyboardButton('〄 Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('Aʙᴏᴜᴛ ⍟', callback_data='about')
        ],[
        InlineKeyboardButton('Cʟᴏsᴇ ✘', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⍟ Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('Aʙᴏᴜᴛ ⍟', callback_data='about'),
        InlineKeyboardButton('Cʟᴏsᴇ ✘', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⍟ Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('〄 Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('Cʟᴏsᴇ ✘', callback_data='close')
        ]]
    )
OWNER_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⍟ Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('〄 Hᴇʟᴘ', callback_data='help'),
        ],[
        InlineKeyboardButton('Cᴏɴᴛᴀᴄᴛ Dᴇᴠ ☯', url=f"https://telegram.dog/KristyX_TG")
        ],[
        InlineKeyboardButton('Aʙᴏᴜᴛ ⍟', callback_data='about'),
        InlineKeyboardButton('Cʟᴏsᴇ ✘', callback_data='close')
        ]]
    )
STATS_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Cʟᴏsᴇ ✘', callback_data='close'),
        InlineKeyboardButton('⍟ Hᴏᴍᴇ', callback_data='home')
        ]]
    )

@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    elif update.data == "owner_info":
        await update.message.edit_text(
            text=OWNER_TEXT,
            disable_web_page_preview=True,
            reply_markup=OWNER_BUTTONS
        )
    else:
        await update.message.delete()
        
# Start Message
@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    user = await bot.get_me()
    mention = user.mention
    await bot.send_message(
        msg.chat.id,
        START_TEXT.format(msg.from_user.mention, mention),
        reply_markup=START_BUTTONS
    )


# Help Message
@Client.on_message(filter("help"))
async def _help(bot: Client, msg: Message):
    await bot.send_message(
        msg.chat.id, HELP_TEXT,
        reply_markup=HELP_BUTTONS
    )


# About Message
@Client.on_message(filter("about"))
async def about(bot: Client, msg: Message):
    await bot.send_message(
        msg.chat.id,
        ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )
