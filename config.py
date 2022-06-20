import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "19303151")
API_HASH = os.getenv("API_HASH", "69fcf6ca06865b043feef7d8948574f5")
SESSION = os.getenv("SESSION", "AgCazyD-wT5PEdUdr9uR0pvoBvsa7GFmea5ZzM5wdXlTdi09YkftzH3XU97xXUZWonNMPFaJC5p7ikd6KHRcp1tHXW_jP_vrspwPDFK294s-ey0P7z8HpwoFJBF1IbWcT81fl4RNAX0u2fYED2YJQIRkei_PfxoPxnOAK841OazrIWKxGaNf2-cIeSkquN5E2AN4NVRVpVvNqdft92IuaTOlRpD0bnXRu66oL38DrU7B8ED-2rqftizwApZkZa-NTzaU9aTasfbxAXxjgIpeOGZ4Q8NFZOdXrOkPMqNkaZvXFSrRXpAjX7dxXIqJaZPho6up-IW1UU0VzYxuVoCEj6XqTB_hRgA")
HNDLR = os.getenv("HNDLR", ".")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "1277157702").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicAndVideo"))
call_py = PyTgCalls(bot)
