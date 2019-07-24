import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class NewEmoji(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_emojis=True)
    async def newemoji(self, ctx, emojiname): 
        await ctx.guild.create_custom_emoji(emojiname, ctx.message.attachments[0].url)
        await ctx.send(f"Created a new emoji! :{emojiname}:")
        
def setup(client):
    client.add_cog(NewEmoji(client))
