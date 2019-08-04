from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

client.run("NjA1MDAwMDI2MjM3OTYwMjA0.XUEuXg.vm0O8fheswPldECjPTFNXmpqANM")
