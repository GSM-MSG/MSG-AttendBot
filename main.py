import asyncio

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


@bot.command(name="독촉")  # 매일 아침 8시 (주말제외?) 개인 DM으로 쓰라고 연락옴
async def follow(ctx):
    dm_channel = await ctx.message.author.create_dm()
    await dm_channel.send(f'{ctx.message.author.mention}님, 출석하세요! 데일리 적고 공유해주세요!')


@bot.command(name="알람")
async def alarm(ctx, duration: int):
    if duration not in [3, 5, 7]:
        await ctx.send("3, 5, 7분 뒤 재알람만 가능합니다.")
        return

    await ctx.send(f"{duration}분 후에 재알람 설정이 되었습니다. **출석**과 **데일리**를 성실하게 해주세요 오늘도 파이팅 ٩( ᐛ )و")
    await asyncio.sleep(duration)
    await ctx.author.send(f"{duration}분이 지났습니다. `/출석`, `/데일리작성` 명령어를 사용하세요.")


@bot.command(name="도움말")
async def helps(ctx):
    embed = discord.Embed(title="도움말",
                          description="**/데일리작성**\n데일리를 적습니다.\n\n**/데일리삭제**\n데일리 내용 모두 삭제합니다.\n\n**/재알람**\n`/알람 "
                                      "3`형식으로 작성합니다. 3,5,7분만 가능합니다.\n\n**/출석**\n출석을 해서 스택을 쌓습니다.\n\n"
                          , color=0xffc0cb)

    await ctx.send(embed=embed)


bot.run(token)
