import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class Moderation(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members)
    async def kick(self, ctx, user : discord.Member, *, reason=None): 
        await ctx.send(ctx.author.toprole.position)
        await ctx.send(user.toprole.position)
        
        
def setup(client):
    client.add_cog(Moderation(client))
