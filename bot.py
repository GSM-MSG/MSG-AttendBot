import asyncio
import logging
import discord
from discord import client
from discord.ext import commands
from attendance import Member, table_init, get_all_attendance_info, scoreboard

from config import timezone

logger = logging.getLogger(__name__)
lock = asyncio.Lock()


async def process_commands(self, message):
    ctx = await self.get_contect(message)
    await self.invoke(ctx)


commands.bot.BotBase.process_commands = process_commands

intents = discord.Intents(messages=True, guilds=True, members=Ture)

