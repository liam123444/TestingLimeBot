import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import random

class Eval(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command(no_pm=True)
    @commands.is_owner()
    async def eval(self, ctx, *, e):
        print(ctx.guild.name)
        try: 
            await ctx.send(f'`{str(eval(e))}`')
        except: 
            await ctx.send("Couldn't run the code.")
        
def setup(client):
    client.add_cog(Eval(client))
