import os
from pytube import YouTube
import discord
import ffmpeg
from discord.ext import commands

class misc(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='play')
    async def play(self,ctx,url):
        guild= ctx.message.guild
        
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

    @commands.command(name='clean')
    @commands.has_permissions(administrator=True)
    async def purge(self,ctx,limit:int = 50):
        if ctx.author.guild_permissions.administrator:
            await ctx.channel.purge(limit=limit)
            await ctx.send(f'Cleared by {ctx.author.mention}')
            await  ctx.message.delete()
        else:
            await ctx.send("Admin power only!")


    @commands.command(name='help')
    async def help(self,ctx):
        embed=discord.Embed(title="Dergbot Help", description="Information on how to use me either @ me or use 'db.'", color=0x6830cf)
        embed.add_field(name="Reddit", value="Top", inline=True)
        embed.add_field(name="Nsfw", value="e621 ,r34 example\n ' db.e621 dragon,-female or db.r34 dragon,-female'", inline=False)
        embed.add_field(name="Fun stuff", value=f"hug example \n'db.hug @user'", inline=False)
        embed.set_thumbnail(url='https://d.furaffinity.net/art/raventhedragon/1564470492/1564470492.raventhedragon_4_-_kaqcfbq.gif')
        embed.set_footer(text="For more Information contact @Raβen Ebonscaly#0432")
        await ctx.message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(misc(bot))