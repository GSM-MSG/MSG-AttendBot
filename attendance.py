import sqlite3
import discord
from datetime import datetime, timedelta
import logging
import pytz
from config import timezone
import os

pytz_timezone = pytz.timezone(timezone)

if not os.path.exists("data"):
    os.makedirs("data")
conn = sqlite3.connect("./data/db.sqlite3", check_same_thread=False)
c = conn.cursor()
logger = logging.getLogger(__name__)

class Member:
    def __init__(self, user: discord.Member):
        if (user is not None):
            self.id = user.id
            self.name = user.display_name
            self.user = user
            self.guild = user.guild.id
        return
