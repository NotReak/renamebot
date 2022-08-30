from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "5376260141:AAE3z4mxpeq0BGDSLOlGkpwetRatBRc-3q0")

APP_ID = int(os.environ.get("APP_ID", "10222724"))

API_HASH = os.environ.get("API_HASH", "31f89c370da1fcd5a528f7a8830f86dc")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
