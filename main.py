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


@bot.command(name="독촉") # 매일 아침 8시 (주말제외?) 개인 DM으로 쓰라고 연락옴
async def follow(ctx):
    dm_channel = await ctx.message.author.create_dm()
    await dm_channel.send(f'{ctx.message.author.mention}님, 데일리 적고 공유해주세요!')


@bot.command(name="도움말")
async def help(ctx):
    embed = discord.Embed(title="도움말",
                          description="**/데일리작성**\n데일리를 적습니다.\n\n**/데일리삭제**\n데일리 내용 모두 삭제합니다.\n\n**/알람**\n다시 알람을 보내서 데일리를 작성하도록 합니다.\n\n**/출석**\n출석을 해서 스택을 쌓습니다.\n\n"
                          , color=0xffc0cb)

    await ctx.send(embed=embed)


bot.run(token)
