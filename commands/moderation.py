import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from discord.utils import get

class Moderation(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user : discord.Member, *, reason=None): 
        await ctx.send(get(ctx.guild.members, id=ctx.author.id).toprole.position)
        await ctx.send(get(ctx.guild.members, id=user.id).toprole.position)
        
        
def setup(client):
    client.add_cog(Moderation(client))
