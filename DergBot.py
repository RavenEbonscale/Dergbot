import discord

import os
from dotenv import load_dotenv
from  discord.ext import commands
from owoify import owoify


Exts = ['Nsfw','reddit','mis','dragon','Economy']
load_dotenv('discord.env')
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix=commands.when_mentioned_or('db.'), help_command=None)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord')
    severs = list(bot.guilds)
    for sever in severs:
        print(f'{bot.user} in connected to {sever}')
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name='Crying Suns'))
    print(owoify('===============Loading furry memes============'))
    print(owoify('===============Loaded furry memes============'))

@bot.event
async def on_message(message):
    await bot.process_commands(message)
for ext in Exts:
        bot.load_extension(f'cog.{ext}')
        print(f'{ext} loaded')

bot.run(TOKEN)

