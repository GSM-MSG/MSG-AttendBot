from main import bot


@bot.command(name="안녕")
async def testHello(ctx):
    await ctx.channel.send('{} 안녕'.format(ctx.author.mention))
