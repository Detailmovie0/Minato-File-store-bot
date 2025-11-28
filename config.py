import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "25059287"))
API_HASH = os.environ.get("API_HASH", "5e7701953107a273724b07f2beaf8f17")


OWNER_ID = int(os.environ.get("OWNER_ID", "6964203412"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://minato:minato@cluster0.lzhzp8x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003223904414"))

FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1002282783745"))

FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1002393557941"))

FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "-1002594005991"))

FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "-1002497307753"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/b1266d63235f95afb3db1-10273b6cbb01406207.jpg")
F_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/95cefa3272feec077b28a-78591fe27d4215c260.jpg")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds


PORT = os.environ.get("PORT", "8050")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6964203412]
    for x in (os.environ.get("ADMINS", "6964203412").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', None) == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "<b></blockquote>Sorry 😐 You can't Message me in personal !\n\n» Management By ➥ </blockquote><a href='https://t.me/moviehub4u_update'><b>M◍viε⁠ ｡Hᴗ⁠b ｡4U 🌿</b></a>\n\n Ownee ➥ <a href='https://t.me/dvl_naruto_06'><b>Ɲ 么 ʀ ᴜ Ƭ͢ ᴏ メ 🌿</b></a></blockquote></b>"

START_MSG = os.environ.get("START_MESSAGE", "<b>Hey {first} Friend I am a Super Advance File Store bot 🌿 \n\n I am created by ➥ 「 <a href='https://t.me/moviehub4u_update'>M◍viε⁠ ｡Hᴗ⁠b ｡4U 🌿</a> 」</b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 {first} You can join our all channels ..\n\n 𝐒𝐨 please join and  “𝐍𝐨𝐰 𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞” 𝐛𝐮𝐭𝐭𝐨𝐧....!")




ADMINS.append(OWNER_ID)
ADMINS.append(6964203412)

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
   

class Txt(object):
    about = f"""<b>My Name :</b> <a href=''>M◍viε⁠ ｡Hᴗ⁠b ｡4U File store bot</a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Update Channel :</b> <a href='https://t.me/moviehub4u_update'>M◍viε⁠ ｡Hᴗ⁠b ｡4U</a>
<b>🛡️ Support Group:</b> <a href='http://t.me/disscus_moviehub4u'>M◍viε⁠ ｡Hᴗ⁠b ｡4U</a>
    
<b>𝖩𝗈𝗂𝗇  ➥ :</b>「 <a href='https://t.me/moviehub4u_update'><b>M◍viε⁠ ｡Hᴗ⁠b ｡4U 🌿</b></a> 」"""


# Tech freak 
# Don't Remove Credit!!!
# Telegram Channel @Tech_freak_tamil
# Developer @devilo7
