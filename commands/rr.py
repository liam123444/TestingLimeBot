import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import random

class RR(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["roulette", "russianroulette"])
    @commands.cooldown(1, 10, BucketType.user)
    async def rr(self, ctx): 
        if random.randint(1, 6) == 3: 
            await ctx.send(":gun: BANG! Oh shit it was the bullet, let me cast my healing spell")

        else:
            await ctx.send(":gun: BANG! The gods want you to live another day, it was just a blank.")

        
def setup(client):
    client.add_cog(RR(client))
