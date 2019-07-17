import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import json
import random

class Testing(commands.Cog): 

    def __init__(self, client):
        self.client = client

        with open(r"commands/creating.json", "r") as f: 
            self.testing = json.load(f)
            
    @commands.command()
    @commands.is_owner()
    async def testtest(self, ctx, wut, alsowut):
        self.testing[str(wut)] = str(alsowut)
        with open(r"commands/creating.json", "w") as f:
            json.dump(self.testing, f, indent=4)
            
    @commands.command()
    @commands.is_owner()
    async def teval(self, ctx, evl): 
        try:
            eval(evl)
        except:
            await ctx.send("Failed to run code")
    
    @commands.command()
    @commands.is_owner()
    async def reval(self, ctx, evl): 
        try:
            await ctx.send(str(eval(evl)))
        except:
            await ctx.send("Failed to run code")
        

    

        
def setup(client):
    client.add_cog(Testing(client))
