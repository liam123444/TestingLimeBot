import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import random

class Diceroll(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["dice", "roll", "rolldice"])
    @commands.cooldown(1, 10, BucketType.user)
    async def diceroll(self, ctx, limit=6):
        await ctx.send(f"I rolled {random.randint(1, limit)}") 


        
def setup(client):
    client.add_cog(Diceroll(client))
