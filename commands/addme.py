import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class Addme(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def addme(self, ctx): 
        await ctx.author.send_friend_request()

        
def setup(client):
    client.add_cog(Addme(client))
