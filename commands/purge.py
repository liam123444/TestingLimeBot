import discord
from discord.ext import commands

class Purge(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=1): 
        await ctx.channel.purge(limit=amount)

        
def setup(client):
    client.add_cog(Purge(client))
