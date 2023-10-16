
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

AttendBot_TOKEN