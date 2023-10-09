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
client = commands.Bot(command_prefix='/', description="도움말 명령어는 /도움", intents=intents)
client.remove_command('help')
table_init


@client.event
async def on_reday():
    activity = discord.Game(name="도움말 명령어는 /도움")
    await  client.change_presence(activity=activity)
    logger.info("Attend Bot is Ready")


@client.check
async def globally_block_dms(ctx):
    return ctx.guild is not None


@client.command(name="등록")
async def register(ctx):
    member = Member(ctx.author)
    logger.info(f"Querying user (id={member.id}, guild={member.guild})'s AttendBot...")
    if not member.exist_db():
        await ctx.channel.send("등록되지 않은 사용자입니다.")
        return


@client.command(name="도움")
async def help_message(ctx):
    await ctx.author.send("```" +
                          "기본\n" +
                          "/등록: 등록하기\n" +
                          "/점수 : 내 점수 확인하기\n" +
                          "/점수 @멘션 : 멘션한 계정의 점수 확인하기\n" +
                          "/순위표 : 점수 순위표 출력하기\n" +
                          "/도움 : 도움말\n" +
                          "\n" +
                          "AttendBotAPIClient 역할\n" +
                          "!점수추가 @멘션 점수 : 계정의 점수를 입력한 점수만큼 추가하기\n" +
                          "\n" +
                          "깃허브 : https://github.com/shk0625/MSG-AttendBot\n" +
                          "```")
    return


