import os
import re
from yt_dlp import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", "17554686"))
    API_HASH = os.environ.get("API_HASH", "afa6bc76814c8d714dd93f7116b4477d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5543601819:AAH2rU_foj5_QVScMFGDNFj_u-R4jrgo23c")
    START_MSG = os.environ.get("START_MSG", "<b>Hi {},\nIam A Simple Youtube to Mp3 Downloader Bot,</b>\n\nSend me Any Songs name with /song command")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/2a35fca576aa49de77c98.jpg")
    OWNER = os.environ.get("OWNER", "shamilhabeeb") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
