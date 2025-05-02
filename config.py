#(©) PythonBotz 




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#Time in seconds for message Auto delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "10"))

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1002361101862"))
#put 0 to disable
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002631555331"))#put 0 to disable
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002207278408"))#put 0 to disable
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1002189440226"))#put 0 to disable

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote> 🍒 ʜᴇʏ !! {mention} ɪ ᴀᴍ ʀɪᴀꜱ~ ʏᴏᴜʀ ʜᴏᴛ ғɪʟᴇ ꜱᴛᴏʀᴇ ǫᴜᴇᴇɴ~ ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ ᴀ ꜱᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜꜱᴇʀꜱ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜᴇᴍ ᴜꜱɪɴɢ ᴀ ᴜɴɪǫᴜᴇ ʟɪɴᴋ~.</blockquote></b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ᴏᴏᴏᴏᴏʜ~ {first}\n\n<b> , ʏᴏᴜ ᴄᴀɴ'ᴛ ᴛᴏᴜᴄʜ ᴍᴇ ʏᴇᴛ...ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴍʏ sᴇᴄʀᴇᴛ ʀᴏᴏᴍ ꜰɪʀꜱᴛ~  ᴛʜᴇɴ ᴄᴏᴍᴇ ʙᴀᴄᴋ ᴛᴏ ᴘʟᴀʏ, ɪ'ʟʟ ʙᴇ ᴡ")

# Start & Fsub Pics ----------------------------------- #

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
PICS = (os.environ.get("PICS", "https://envs.sh/Vx5.jpg https://envs.sh/VxL.jpg https://envs.sh/Vxc.jpg https://envs.sh/V8O.jpg https://envs.sh/V8m.jpg https://envs.sh/V8X.jpg https://envs.sh/V8y.jpg")).split() #Required

# Start & Fsub Pics ----------------------------------- #

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = """<b><blockquote>🍒 ʀɪᴀꜱ' ɴᴀᴜɢʜᴛʏ ᴀʀᴄʜɪᴠᴇ ꜱᴛᴀᴛꜱ</b>

• <b>ʙᴏᴛ ᴜᴘᴛɪᴍᴇ:</b> {uptime}

<code>ᴏɴʟʏ ᴍʏ ᴅᴀʀʟɪɴɢ ᴍᴀꜱᴛᴇʀ ᴄᴀɴ ᴘʟᴀʏ ᴡɪᴛʜ ᴛʜᴇꜱᴇ ꜱᴇᴄʀᴇᴛꜱ~</code></blockquote>"""
USER_REPLY_TEXT = "<b><blockquote>ᴏᴏᴘs~ 🙃 ᴏɴʟʏ ᴍʏ ᴍᴀꜱᴛᴇʀ ᴄᴀɴ ꜱᴛᴏʀᴇ ꜰɪʟᴇꜱ ɪɴ ᴍᴇ~  ʏᴏᴜ'ʀᴇ ɴᴏᴛ ʜɪᴍ, ʙᴀʙʏ~<\blockquote><\b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
