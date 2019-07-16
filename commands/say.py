import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class Say(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def say(self, ctx, *, say):
        await ctx.send(f'`{say}`') 
        await ctx.message.delete()

        
def setup(client):
    client.add_cog(Say(client))
