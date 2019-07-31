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

@bot.command()
async def bosyuu(ctx):
    await ctx.send('pong')

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('みゃおん')
        # メンバーのリストを取得して表示
    if message.content == '/members':
        print(message.guild.members)
        # 役職のリストを取得して表示
    if message.content == '/roles':
        print(message.guild.roles)
        # テキストチャンネルのリストを取得して表示
    if message.content == '/text_channels':
        print(message.guild.text_channels)
        # ボイスチャンネルのリストを取得して表示
    if message.content == '/voice_channels':
        print(message.guild.voice_channels)
        # カテゴリチャンネルのリストを取得して表示
    if message.content == '/category_channels':
        print(message.guild.categories)
    if message.content == '/team':
        vc = client.get_channel(600258156001624064)
        members = vc.members
        print(members)


client.run("NjA1MDAwMDI2MjM3OTYwMjA0.XUEuXg.vm0O8fheswPldECjPTFNXmpqANM")
