import asyncio

from datetime import datetime
import connection
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
load_dotenv()

token = os.getenv('AttendBot_TOKEN')
channel_id = os.getenv('CHANNEL_ID')

connection = connection.Connection()
conn, cur = connection.getConnection()


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    channel = bot.get_channel(int(channel_id))

    if channel:
        command = bot.get_command("도움말")
        if command:
            await command.callback(channel)


@bot.command(name="안녕")
async def testHello(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention}님, 나도 안녕!', reference=ctx.message)


@bot.command(aliases=['독촉', 'dc'])  # 상대방이 멘션하는 사람에게 독촉 DM 대신 보내기 가능
async def follow(ctx, user: discord.Member):
    if user:
        await user.send(f"{user.mention}님, 출석하세요! 데일리를 적고 공유해주세요!")
    else:
        await ctx.send("사용자를 찾을 수 없습니다.")


@bot.command(aliases=['알람', 'al'])
async def alarm(ctx, duration: int = None):
    if duration is None or duration not in [3, 5, 7]:
        await ctx.send("3, 5, 7분 뒤 재알람만 가능합니다.`/알람` 형식으로 입력해주세요.")
        return

    await ctx.send(f"{ctx.message.author.mention}님, {duration}분 후에 재알람 설정이 되었습니다. **출석**과 **데일리**를 성실하게 해주세요 오늘도 파이팅 "
                   f"٩( ᐛ )و")
    await asyncio.sleep(duration)
    await ctx.author.send(f"{ctx.message.author.mention}님, {duration}분이 지났습니다. `/출석`, `/데일리작성` 명령어를 사용하세요.")


@bot.command(aliases=['출석', 'at'])
async def attend(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    conn, cur = connection.getConnection()
    sql = f"SELECT * FROM daily WHERE did=%s"
    cur.execute(sql, (str(member.id),))
    rs = cur.fetchone()
    today = datetime.now().strftime('%Y-%m-%d')

    if rs is not None and str(rs.get('date')) == today:
        await ctx.message.delete()
        await ctx.channel.send(f'> {member.display_name}님은 이미 출석체크를 했어요!')
        return

    if rs is None:
        sql = "INSERT INTO daily (did, count, date) values (%s, %s, %s)"
        cur.execute(sql, (str(member.id), 1, today))
        conn.commit()
    else:
        sql = 'UPDATE daily SET count=%s, date=%s WHERE did=%s'
        cur.execute(sql, (rs['count'] + 1, today, str(member.id)))
        conn.commit()
    await ctx.channel.send(f'> {member.display_name}님의 출석이 확인되었어요! 이제 데일리를 작성해볼까요?')


@bot.command(aliases=['순위', 'rk'])  # count 10개당 n점 환산으로 순위표에 등재됨.
async def standing(ctx):
    embed = discord.Embed(title="순위표", description=discord.utils.escape_markdown(scoreboard(ctx.author.guild)))


@bot.command(aliases=['도움말', 'hp'])
async def helps(ctx):
    embed = discord.Embed(title="도움말",
                          description="**/작성**\n데일리를 적습니다.\n\n"
                                      "**/삭제**, **/dd**\n데일리 내용 모두 삭제합니다.\n\n"
                                      "**/알람**\n`/알람 3`, `/al 3`형식으로 작성합니다. 3,5,7분만 가능합니다.\n\n"
                                      "**/출석**\n`/출석`을 해서 스택을 쌓습니다. `/출석 @상대` 기능으로 출석여부를 파악할 수 있습니다.\n\n "                                      
                                      "**/순위표**\n현재 출석률을 확인합니다.\n\n"
                                      "**/독촉**\n`/독촉 @상대`형식으로 사용합니다. 멘션 대상자에게 독촉 DM을 봇이 대신 보내줍니다.\n\n"
                          , color=0xffc0cb)

    await ctx.send(embed=embed)


@bot.command(aliases=['루틴', 'rt'])
async def routine(ctx):
    embed = discord.Embed(title="출석체크라도 하세요!!!!!!",
                          description="포인트가 얻고 싶지 않으신가요?\n\n순위표에 1등 한 번 찍어보셔야죠?\n\n이 쉬운걸..안 해?\n\n"
                          , color=0xffc0cb)
    await ctx.send(embed=embed)


bot.run(token)
