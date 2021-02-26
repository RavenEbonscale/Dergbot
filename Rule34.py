import requests as rq
import xml.etree.ElementTree as ET
import random



class Rule34:


    def __init__(self):
        self.limit= 100


    def Rule34_Get(self,tags):
        URL= f'https://rule34.xxx/index.php?page=dapi&s=post&q=index&tags={tags}'
        urls= []
        header = {
            'tags': 'dragon'
        }
        s = rq.session()
        data = s.get(URL,stream=True,headers=header)
        print(data.status_code)
        tree = ET.fromstring(data.content)
        #ET.dump(tree)
        for post in tree:
            porn = post.get('file_url')
            urls.append(porn)
        return urls

    def Rule34(self,tags):
        urls = self.Rule34_Get(tags)
        url = random.choice(urls)
        return(url)






