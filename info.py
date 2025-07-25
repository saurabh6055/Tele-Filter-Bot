
import re
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')


def is_enabled(value, default):
    value = value.lower()
    if value in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value in ["false", "no", "0", "disable", "n"]:
        return False
    return default


# ─── Bot Info ───────────────────────────────────────────
SESSION = environ.get('SESSION', 'Tele_Filter')
API_ID = int(environ.get('API_ID', '28199593'))
API_HASH = environ.get('API_HASH', 'b76f22d4916774d1942cb478323249e3')
BOT_TOKEN = environ.get('BOT_TOKEN', "8498307351:AAGXlfIXljtPvp_8a7Zjs6M2nmvZrL-4YJs")


# ─── Bot Settings ───────────────────────────────────────
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = environ.get(
    'PICS',
    'https://envs.sh/R3g.jpg https://envs.sh/R3H.jpg https://envs.sh/R3N.jpg https://envs.sh/R3v.jpg https://envs.sh/R39.jpg'
).split()

NOR_IMG = environ.get("NOR_IMG", "https://envs.sh/R3g.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://envs.sh/R3g.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/7b0ba2952ec098bb46997.jpg")
VRFIED_IMG = environ.get("VRFIED_IMG", "https://envs.sh/R3g.jpg")
VRFY_IMG = environ.get("VRFY_IMG", "https://envs.sh/R3N.jpg")


# ─── Admins / Users / Channels ──────────────────────────
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '0').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]

auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002077365469')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002217291160')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))


# ─── MongoDB ─────────────────────────────────────────────
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://:@cluster0.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "deepu_db")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telefilter')


# ─── Shortlink & Other Settings ─────────────────────────
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'adlinkfly.in')
SHORTLINK_API = environ.get('SHORTLINK_API', 'af77f68713ff5ec1e9e7ahsuskaqkcc29e85ceb855a')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled(environ.get('MAX_BTN', "True"), True)
PORT = environ.get("PORT", "8080")

GRP_LNK = environ.get('GRP_LNK', 'https://t.me/ur_movie_group')
SPRT_CHNL = environ.get('SPRT_CHNL', 'https://t.me/kissuxbots')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/kissuxbots')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/bot_making_tips')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', 'https://t.me/kissuxbots')
MSG_ALRT = environ.get('MSG_ALRT', 'ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : 𓆩•𝐊𝐢𝐬𝐬𝐮💞•𓆪')


# ─── Display Configurations ─────────────────────────────
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', "-1002591123448"))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'deepu_support')

P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
IMDB = is_enabled(environ.get('IMDB', "True"), False)
AUTO_FFILTER = is_enabled(environ.get('AUTO_FFILTER', "True"), True)
AUTO_DELETE = is_enabled(environ.get('AUTO_DELETE', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

REQ_GRP = environ.get('REQ_GRP', 'https://t.me/ur_movie_group')
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '-1002722911746').split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "False"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)


# ─── Constants ──────────────────────────────────────────
LANGUAGES = [
    "malayalam", "", "tamil", "", "english", "", "hindi", "",
    "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""
]

SEASONS = [
    "season 1", "season 2", "season 3", "season 4", "season 5",
    "season 6", "season 7", "season 8", "season 9", "season 10"
]

QUALITIES = [
    "360P", "", "480P", "", "720P", "",
    "1080P", "", "1440P", "", "2160P"
]


# ─── Debug Log Output ───────────────────────────────────
LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += "IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n"
LOG_STR += "P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n"
LOG_STR += "SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n"
LOG_STR += f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n"
LOG_STR += "Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n"
LOG_STR += "Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n"
LOG_STR += f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n"
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
