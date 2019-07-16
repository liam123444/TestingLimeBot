import discord
from discord.ext import commands

class Listroles(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def listroles(self, ctx): 
        rolem = ""
        for roles in ctx.guild.roles:
            rolem += f"\n <@&{roles.id}> - \<@&{roles.id}>"

        embed = discord.Embed(title="Roles", description=rolem, color=0x00ff00)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
        

        
def setup(client):
    client.add_cog(Listroles(client))
