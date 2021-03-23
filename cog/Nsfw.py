import os
from  discord.ext import commands
from cog.e621 import e621
from cog.Rule34 import Rule34
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv('discord.env')

e6 = e621(os.getenv('e621login'),os.getenv('e621api-key'),os.getenv('e621User-Agent'))
r34 = Rule34()

class Nsfw(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name= 'e621t')
    @commands.is_nsfw()
    async def e621(self,ctx,tags,num =1 ):
        if 'wholsome' not in tags:
            
            tags = tags.replace(',','+')
            images = await e6.get_image(tags,num)

            await ctx.message.channel.send(embed=images)
            print(f'sent to {ctx.message.channel} ^.^')

        else:
            await ctx.message.channel.send('Fuck off {}'.format(ctx.message.author.mention()))

    @commands.command('e621a')
    @commands.is_nsfw()
    async def e621_list(self,ctx,tags,num):
            if 'wholsome' not in tags:
                for num in range(num):
                    tags = tags.replace(',','+')
                    image = await e6.get_animation(tags)
                    await ctx.message.channel.send(image)
                    print(f'sent to {ctx.message.channel} ^.^')

            else:
                await ctx.message.channel.send('Fuck off @{ctx.message.author}')


    @commands.command('r34')
    @commands.is_nsfw()
    async def Rule34(self,ctx,tags):
        channel = ctx.message.channel
        tags = tags.replace(',','+')
        image = r34.Rule34(tags)
        await channel.send(image)
        print(f'sent to Channel: {channel} in Guild: {ctx.message.guild}')

def setup(bot):
    bot.add_cog(Nsfw(bot))