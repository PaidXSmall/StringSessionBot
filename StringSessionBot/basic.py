from data import Data
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, Message, InlineKeyboardButton, CallbackQuery
from pyrogram.enums.parse_mode import ParseMode
import re, asyncio, time, shutil, psutil, os, sys, random

def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)


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

    
START_TEXT = """
<b> Hᴇʟʟᴏ {}

Wᴇʟᴄᴏᴍᴇ ᴛᴏ {}

Iғ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴛʀᴜsᴛ ᴛʜɪs ʙᴏᴛ, 
𝟷) sᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪs ᴍᴇssᴀɢᴇ
𝟸) ᴅᴇʟᴇᴛᴇ ᴛʜɪs ᴄʜᴀᴛ
Sᴛɪʟʟ ʀᴇᴀᴅɪɴɢ?

Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ (ᴇᴠᴇɴ ᴠᴇʀsɪᴏɴ 𝟸) ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ. Usᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ !

Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : <a href='https://t.me/Abt_Kristy'>Kʀɪsᴛʏ கிறிஸ்டி</a>
</b>
"""

HELP_TEXT = """
<b> 
✨ **Available Commands** ✨

➤ /about - About The Bot
➤ /help - This Message
➤ /start - Start the Bot
➤ /generate - Generate Session
➤ /cancel - Cancel the process
➤ /restart - Cancel the process

Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ (Oʀ) Rᴇᴘᴏʀᴛ Bᴜɢꜱ : <a href='https://t.me/KristyX_TG'>Kʀɪsᴛʏ கிறிஸ்டி | 🇮🇳 |</a> </b>"""

ABOUT_TEXT = """<b>
✯ Mʏ Nᴀᴍᴇ: Sᴛʀɪɴɢ Sᴇssɪᴏɴ Bᴏᴛ
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
        InlineKeyboardButton("🔥Sᴛᴀʀᴛ Gᴇɴᴇʀᴀᴛɪɴɢ Sᴇssɪᴏɴ 🔥", callback_data="generate")
        ],[
        InlineKeyboardButton('✇ Uᴘᴅᴀᴛᴇs ', url=f"https://t.me/PeterXCLouD"),
        InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ ⌬', url=f"https://t.me/PeterXCLouD")
        ],[
        InlineKeyboardButton('♚ Bᴏᴛ Oᴡɴᴇʀ', callback_data="owner_info")
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
    elif query == "generate":
        await callback_query.answer()
        await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                #await callback_query.answer("Please note that the new type of string sessions may not work in all bots, i.e, only the bots that have been updated to pyrogram v2 will work!", show_alert=True)
                await generate_session(bot, callback_query.message)
                """
            # Maybe in future it'll come back.
            elif query == "pyrogram1":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, old_pyro=True)
                """
            elif query == "pyrogram_bot":
                await callback_query.answer("Please note that this bot session will be of pyrogram v2", show_alert=True)
                await generate_session(bot, callback_query.message, is_bot=True)
            elif query == "telethon_bot":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
            elif query == "telethon":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))
    else:
        await update.message.delete()

ERROR_MESSAGE = "Oops! An exception occurred! \n\n**Error** : {} " \
            "\n\nPlease visit @StarkBotsChat if this message doesn't contain any " \
            "sensitive information and you if want to report this as " \
            "this error message is not being logged by us!"
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

#restaert command 
@Client.on_message(filters.command("restart") & filters.private)
async def stop_button(bot, message):
    msg = await bot.send_message(text="**🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...**", chat_id=message.chat.id)       
    await asyncio.sleep(3)
    await msg.edit("**✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴**")
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(filters.command("statss"))          
async def stats(bot, update):
    currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - BOT_START_TIME))
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    ms_g = f"""<b><u>Bot Statistics</b></u>

• Uptime: <code>{currentTime}</code>
• CPU Usage: <code>{cpu_usage}%</code>
• RAM Usage: <code>{ram_usage}%</code>
• Total Disk Space: <code>{total}</code>
• Used Space: <code>{used} ({disk_usage}%)</code>
• Free Space: <code>{free}</code>
"""

    msg = await bot.send_message(chat_id=update.chat.id, text="__Processing...__", parse_mode=enums.ParseMode.MARKDOWN)         
    await msg.edit_text(text=ms_g, parse_mode=enums.ParseMode.HTML, reply_markup=STATS_BUTTONS)
