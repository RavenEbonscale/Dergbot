import re
from discord import Embed
import requests as rq
import random


class e621:
    user_agent= None
    Api = None
    username = None


    def __init__(self,username,Api_key,useragent):
        self.exts = re.compile("\/*.(jpg|gif|png|mp4|webm)$")
        self.headers={    'User-Agent' :useragent ,
                            'login' :username ,
                            'api-key':Api_key}



    async def get_image(self,tags):
        urls= await geturls(tags,safe= False,headers=self.headers,exts=self.exts)
        url = random.choice(urls)
        embed =Embed()
        embed.set_image(url=url)
        return embed

    async def get_animation(self,tags):
        urls= await geturls(tags,True,False,headers=self.headers,exts=self.exts)
        url = random.choice(urls)
        return url
class e926:
    user_agent= None
    Api = None
    username = None


    def __init__(self,username,Api_key,useragent):
        self.exts = re.compile("\/*.(jpg|gif|png|mp4|webm)$")
        self.headers={    'User-Agent' :useragent ,
                            'login' :username ,
                            'api-key':Api_key}



    async def get_image(self,tags):
        urls= await geturls(tags,safe= True,headers=self.headers,exts=self.exts)
        url = random.choice(urls)
        embed =Embed()
        embed.set_image(url=url)
        return embed

    async def get_animation(self,tags):
        urls= await geturls(tags,True,True,headers=self.headers,exts=self.exts)
        url = random.choice(urls)
        return url










async def geturls(tags,ani=False,safe= True,headers =None,exts =None):
    img_urls= []
    if safe ==True:
        site = 'e926'
    else:
        site= 'e621'
    if ani == False:
        URL = f'https://{site}.net/posts.json/?tags={tags}&limit=100'
        print(URL)
    else:
        URL =f'https://{site}.net/posts.json/?tags={tags}+animation&limit=100'
        print(URL)
    load = rq.get(URL, headers=headers).json()
    e621 = load['posts']
    for  post in e621:
        if 'file' in post:
            if post not in img_urls:
                #coverts the size of the files into megabytes
                size= post['file']['size']/1e+6
                url =post['file']['url']
                #discord has an upload size of 8mb for bots
                if url != None and size <= 8 :
                    isMatch = len(exts.findall((url))) > 0
                    if isMatch:
                        img_urls.append(url)
    return img_urls
