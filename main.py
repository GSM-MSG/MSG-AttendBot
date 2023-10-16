import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
load_dotenv()

token = os.getenv('AttendBot_TOKEN')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run(token)


