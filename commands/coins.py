import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from discord.utils import get
import asyncpg

class Coins(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def addcoins(self, ctx, coins:int, u:discord.Member = "None"): 
        if u == "None":
            user = await self.client.pg_con.fetch("SELECT * FROM users WHERE id = $1", str(ctx.author.id))
            name = ctx.author.name
        else:
            user = await self.client.pg_con.fetch("SELECT * FROM users WHERE id = $1", str(u.id))
            name = u.name
        
        if not user: 
            await self.client.pg_con.execute("INSERT INTO users (id, coins) VALUES ($1, 0)", str(u.id))
        
        if u == "None":
            user = await self.client.pg_con.fetchrow("SELECT * FROM users WHERE id = $1", str(ctx.author.id))
        else:
            user = await self.client.pg_con.fetchrow("SELECT * FROM users WHERE id = $1", str(u.id))
            
        await self.client.pg_con.execute("UPDATE users SET coins = $1 WHERE id=$2", user['coins'] + coins, user['id'])
        await ctx.send(f"{name} has been given {coins} coins!")

    @commands.command()
    async def coins(self, ctx):
        user = await self.client.pg_con.fetch("SELECT * FROM users WHERE id = $1", str(ctx.author.id))
        print(user[0])
        if not user: 
            await self.client.pg_con.execute("INSERT INTO users (id, coins) VALUES ($1, 0)", str(ctx.author.id))

        user = await self.client.pg_con.fetchrow("SELECT * FROM users WHERE id = $1", str(ctx.author.id))
        await ctx.send(f"You have {user['coins']} coins!")



        
def setup(client):
    client.add_cog(Coins(client))
