import re
import requests as rq
from tqdm import tqdm
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

    def geturls(self,tags,ani=False):
        img_urls= []
        if ani == False:
            URL = f'https://e621.net/posts.json/?tags={tags}&limit=100'
            print(URL)
        else:
            URL =f'https://e621.net/posts.json/?tags={tags}+animation&limit=100'
            print(URL)
        load = rq.get(URL, headers=self.headers).json()
        e621 = load['posts']
        for  post in tqdm(e621):
            if 'file' in post:
                if post not in img_urls:
                    #coverts the size of the files into megabytes
                    size= post['file']['size']/1e+6
                    url =post['file']['url']
                    #discord has an upload size of 8mb for bots
                    if url != None and size <= 8 :
                        isMatch = len(self.exts.findall((url))) > 0
                        if isMatch:
                            print(size)
                            img_urls.append(url)
        return img_urls
    def get_image(self,tags):
        urls= self.geturls(tags)
        url = random.choice(urls)
        return url

    def get_animation(self,tags,spam = False):
        urls= self.geturls(tags,True)
        url = random.choice(urls)
        return url

