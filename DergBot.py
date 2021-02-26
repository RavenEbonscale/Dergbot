import discord,os
from dotenv import load_dotenv
from  discord.ext import commands
from pytube import YouTube
import ffmpeg
Exts = ['Porn','reddit']
load_dotenv('discord.env')
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'))

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord')
    severs = list(bot.guilds)
    for sever in severs:
        print(f'{bot.user} in connected to {sever}')
    for ext in Exts:
        bot.load_extension(ext)
        print(f'{ext} loaded')

@bot.event
async def on_message(message):
    if message.content == 'good bot':
        await message.channel.send('Thank you')
    if message.content == 'bad bot':
        await message.channel.send('SOwOry,Miwester')
    if 'how are you' in message.content:
        await message.channel.send('Not bad but my life is grand')
    await bot.process_commands(message)

@bot.command(name='play')
async def play(ctx,url):
    guild= ctx.message.guild
    print(guild)
    song_check = os.path.isfile(f'{guild}.mp3')
    try:
        if song_check:
            os.remove(f'{guild}.mp3')
    except  PermissionError:
        await ctx.send("Wait for current audio to end")
        return
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download()
    for file in os.listdir('./'):
        if file.endswith(".mp4"):
            os.rename(file, f'{guild}.mp3')
    channel = ctx.message.author.voice.channel
    vc = await  channel.connect()
    print('Joined')
    server = ctx.message.guild
    voice_client = server.voice_client
    player = vc.play(discord.FFmpegPCMAudio(f'{guild}.mp3'))
    print('Playing')

@bot.command(name='clean')
@commands.has_permissions(administrator=True)
async def purge(ctx,limit:int = 50):
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.purge(limit=limit)
        await ctx.send(f'Cleared by {ctx.author.mention}')
        await  ctx.message.delete()
    else:
        await ctx.send("Admin power only!")

bot.run(TOKEN)