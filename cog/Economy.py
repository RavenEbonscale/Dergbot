import json
import discord
import os

from discord.ext import commands

#To-do
#create Json

class economy(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_member_join(self,member):

        with open('.\\cog\\json-files\\users.json','r') as j:
            users = json.load(j)

        await self.update_json(users,member)

        with open('.\\cog\\json-files\\users.json','w') as j:
            json.dump(users,j)


    @commands.Cog.listener()
    async def on_message(self,message):
        with open('.\\cog\\json-files\\users.json','r') as j:
            users = json.load(j)

        await self.update_json(users,message.author)
        await self.add_exp(users,message.author,5)
        await self.level_up(users,message.author,message.channel)

        with open('.\\cog\\json-files\\users.json','w') as j:
            json.dump(users,j)


    async def update_json(self,users,user):
        if not str(user.id) in users:
            users[str(user.id)]={}
            users[str(user.id)]['experience']= 0
            users[str(user.id)]['level'] = 1
            users[str(user.id)]['inv'] = []
            users[str(user.id)]['inv'].append('dragon')

    async def add_exp(self,users,user,xp):
        #print(f"starting xp {users[user.id]['experience'] }")
        users[str(user.id)]['experience'] += xp
        #print(f"ending xp {users[user.id]['experience'] }")

    async def level_up(self,users,user,channel):
        experience = users[str(user.id)]['experience']
        lvl_start = users[str(user.id)]['level']
        lvl_end =int(experience ** (1/4))

        if lvl_start < lvl_end:
            users[str(user.id)]['level'] += 1
            users[str(user.id)]['inv'].append('hug')


            #await self.bot.send_message(channel,'fuck you')
            print('someone leveled up')

def setup(bot):
    bot.add_cog(economy(bot))