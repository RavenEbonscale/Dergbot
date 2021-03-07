from discord.embeds import Embed
import os
from dotenv import load_dotenv
from random import choice
from cog.e621 import e926
from discord.ext import commands

#add list of url of sfw draons
#add diffrent fucntions
#Dragon gifs?
e6 = e926(os.getenv('e621login'),os.getenv('e621api-key'),os.getenv('e621User-Agent'))



class dragon(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.hug_url = ['https://media1.giphy.com/media/1poXsrQ2sNEWifospK/giphy.gif?cid=ecf05e47qf9ssupyfoqpvmcrebcqel966k4pja7s2n2iwf8i&rid=giphy.gif']

    @commands.command()
    async def hug(self,ctx,person):
        if '@' in person:
            #random pick from an list of hug gifs-need more urls
            e = Embed()
            e.set_image(url=choice(self.hug_url))
            #send
            await ctx.message.channel.send( f'{ctx.message.author.display_name} sent {person} a hug',embed=e)
        else:
            await ctx.message.channel.send('Sorry you need to mention someone Owo')

    @commands.command()
    async def e926(self,ctx,tags):
            tags = tags.replace(',','+')
            images = await e6.get_image(tags)
            await ctx.message.channel.send(embed=images)
            print(f'sent to {ctx.message.channel} ^.^')




















def setup(bot):
    bot.add_cog(dragon(bot))