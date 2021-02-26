import os
from  discord.ext import commands
from discord.ext.commands.core import command
from e621 import e621
from Rule34 import Rule34
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv('discord.env')

e6 = e621(os.getenv('e621login'),os.getenv('e621api-key'),os.getenv('e621User-Agent'))
r34 = Rule34()

class Porn(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name= 'e6')
    async def e621(self,ctx,tags):
        if str(ctx.message.channel) == 'e621':
            if 'wholsome' not in tags:
                tags = tags.replace(',','+')
                images = e6.get_image(tags)
                await ctx.message.channel.send(images)
                print(f'sent to {ctx.message.channel} ^.^')

            else:
                await ctx.message.channel.send('Fuck off @{ctx.message.author}')
        else:
            await ctx.send('please use e621 channel OwO')

    @commands.command('e6a')
    async def e621_list(self,ctx,tags):
        if str(ctx.message.channel) == 'e621':
            if 'wholsome' not in tags:
                tags = tags.replace(',','+')
                image = e6.get_animation(tags)
                await ctx.message.channel.send(image)
                print(f'sent to {ctx.message.channel} ^.^')

            else:
                await ctx.message.channel.send('Fuck off @{ctx.message.author}')
        else:
            await ctx.send('please use e621 channel OwO')

    @commands.command('r34')
    async def Rule34(self,ctx,tags):
        channel = ctx.message.channel
        tags = tags.replace(',','+')
        image = r34.Rule34(tags)
        await channel.send(image)
        print(f'sent to Channel: {channel} in Guild: {ctx.message.guild}')

def setup(bot):
    bot.add_cog(Porn(bot))