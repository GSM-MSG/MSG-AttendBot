import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
# intents.messages_content = True
intents.messages = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run('TOKEN')
