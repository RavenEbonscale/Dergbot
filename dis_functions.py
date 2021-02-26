import random,os
import requests as rq
from dotenv import load_dotenv
load_dotenv('discord.env')

headers = {
    'User-Agent' : os.getenv('e621User-Agent'),
    'login' :os.getenv('e621login') ,
    'api-key':os.getenv('e621api-key')}

async def e621(tags):
    tags = tags
    url=[]
    load = rq.get(f'https://e621.net/posts.json/?tags={tags}&limit=10000',headers= headers).json()
    E621 = load['posts']
    for post in E621:
        if post not in url:
            url.append(post['file']['url'])
    image = random.choice(url)
    return (image)

