import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from discord.utils import get
import asyncpg

class Addreactionrole(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def createreactionrole(self, ctx, msgid:str, roleid:str, emoji:str): 
        rr = await self.client.pg_con.fetch("SELECT * FROM reactionroles WHERE channelid=$1 AND messageid=$2 AND emoji=$3", str(ctx.channel.id), msgid, emoji)
        if len(rr) > 0: 
            await ctx.send("This message already has a reaction role assigned to it with this emoji.")
            return

        try:
            message = await ctx.channel.fetch_message(int(msgid))
        except: 
            await ctx.send("I couldn't find that message id in this channel, please make sure you're using the command in the right channel and you have the correct message id")
            return

        role = get(ctx.guild.roles, id=int(roleid)) 
        if role == None: 
            await ctx.send("I couldn't find a role in the server with that ID, please make sure you have the correct role id")
        
        try:
            await message.add_reaction(emoji)
        except: 
            await ctx.send("That's not an emoji!")
            return

        await self.client.pg_con.execute("INSERT INTO reactionroles (messageid, roleid, channelid, emoji) VALUES ($1, $2, $3, $4)", msgid, roleid, str(ctx.channel.id), emoji)
        await ctx.send("Successfully created a reaction role! :white_check_mark:")
        


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload): 
        rr = await self.client.pg_con.fetch("SELECT * FROM reactionroles WHERE messageid=$1 AND emoji=$2", str(payload.message_id), payload.emoji.name)
        if len(rr) == 0:
            return

        rr = rr[0]
        print(payload.__dir__())
        guild = get(self.client.guilds, id=payload.guild_id)
        user = get(guild.members, id=payload.user_id)
        role = get(guild.roles, id=int(rr["roleid"]))
        await user.add_roles(role)


        
def setup(client):
    client.add_cog(Addreactionrole(client))
