import praw,re,os
import concurrent.futures

from dotenv import load_dotenv
from discord.ext import commands
load_dotenv('discord.env')

img_exts= re.compile("\/*.(jpg|jpeg|png|gif|mp4|gifv)$")

class Reddit_fun():
    def __init__(self):
        pass
    def Urls(self,submision):
        sub_url = submision.url
        isMatch = len(img_exts.findall(sub_url)) > 0
        if sub_url.startswith('https://gfycat.com/') or sub_url.startswith('https://redgifs.com/'):
            if sub_url.startswith('https://gfycat.com/'):
                reurl =sub_url.replace('https://gfycat.com/', 'https://giant.gfycat.com/')
                newurl = f'{reurl}.gif'
                print(newurl)
                return newurl
            else:
                try:
                    newurl = submision.preview['reddit_video_preview']['fallback_url']
                    return newurl
                except :
                        pass
        else:
            if isMatch:
                return sub_url
    def Urls_Text(self,submision):
        sub_url = submision.url
        return sub_url
    async def geturls(self,submissions,Text):
        urls= []
        if Text == False:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for url in executor.map(self.Urls,submissions):
                    urls.append(url)
        else:      
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for url in executor.map(self.Urls_Text,submissions):
                    urls.append(url)

        return urls


class Reddit(commands.Cog):
    def __init__(self):
        self.reddit_fun = Reddit_fun()
        self.reddit = praw.Reddit(client_id= os.getenv('client_id') ,
                                client_secret = os.getenv('client_secret'),
                                user_agent = 'SubBot created by @Raven_Ebonscale')

    @commands.command(name='top')
    async def top_iamges(self,ctx,sub,num= 10,Text=False):
        try:
            if num <= 200:
                submissions = list(self.reddit.subreddit(sub).hot(limit = int(num)))
                #checks to make sure there is an actual url in the list or else there will be an endless loop
                urls = await self.reddit_fun.geturls(submissions,Text)
                if len(urls) != 0:
                    for url in urls:
                        try:
                            await ctx.message.channel.send(url)
                        except:
                            pass
                else:
                    await ctx.send('Sorry this sub dosent have any links i can use')
                print(f'sent to {ctx.message.channel} @ {ctx.message.guild} ^.^')
        except commands.CommandInvokeError as e:
            pass

    @commands.command(name='topt')
    async def top_text(self,ctx,sub,num= 10,Text=True):
        try:
            if num <= 200:
                submissions = list(self.reddit.subreddit(sub).hot(limit = int(num)))
                #checks to make sure there is an actual url in the list or else there will be an endless loop
                urls = await self.reddit_fun.geturls(submissions,Text)
                if len(urls) != 0:
                    for url in urls:
                        try:
                            await ctx.message.channel.send(url)
                        except:
                            pass
                else:
                    await ctx.send('Sorry this sub dosent have any links i can use')
            else:
                print(f'sent to {ctx.message.channel} @ {ctx.message.guild} ^.^')
        except commands.CommandInvokeError as e:
            print(e)

def setup(bot):
    bot.add_cog(Reddit())