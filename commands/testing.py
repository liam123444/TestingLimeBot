import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import json
import random

class Testing(commands.Cog): 

    def __init__(self, client):
        self.client = client

        with open(r"commands\creating.json", "r") as f: 
            self.testing = json.load(f)
            
    @commands.command()
    async def testtest(self, ctx, wut, alsowut):
        self.testing[str(wut)] = str(alsowut)
        with open(r"commands\creating.json", "w") as f:
            json.dump(self.testing, f, indent=4)
        

    

        
def setup(client):
    client.add_cog(Testing(client))
