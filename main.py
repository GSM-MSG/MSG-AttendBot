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


@bot.command(name="안녕")
async def testHello(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention}님, 나도 안녕!', reference=ctx.message)


@bot.command(name="데일리")
async def daily(ctx):
    dm_channel = await ctx.message.author.create_dm()
    await dm_channel.send(f'{ctx.message.author.mention}님, 데일리 적고 공유해주세요!')

bot.run(token)
