import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class Ping(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def ping(self, ctx): 
        await ctx.send(f'Pong! {round(self.client.latency*1000)}ms')

    @commands.command()
    async def pong(self, ctx):
        await ctx.send(f'Ping! <@{ctx.author.id}>')
        
def setup(client):
    client.add_cog(Ping(client))
