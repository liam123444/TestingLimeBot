import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import random
import asyncpg
import math

class RR(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["roulette", "russianroulette"])
    @commands.cooldown(1, 10, BucketType.user)
    async def rr(self, ctx): 
        user = await self.client.pg_con.fetch("SELECT * FROM users WHERE id = $1", str(ctx.author.id))
        if not user: 
            await self.client.pg_con.execute("INSERT INTO users (id, coins) VALUES ($1, 0)", str(ctx.author.id))
            ctx.send("You don't have any coins to use this command.")
        user = user[0]

        if random.randint(1, 6) == 3: 
            await ctx.send(f":gun: BANG! It was the bullet, I revived you but someone stole some of the cash while you were out.\n**(You lost {math.ceil(user['coins']/2)} coins)**")
            await self.client.pg_con.execute("UPDATE users SET coins = $1 WHERE id=$2", user['coins'] - math.ceil(user['coins']/2), str(ctx.author.id))    

        else:
            await ctx.send(":gun: BANG! The gun shot out coins! It must hurt but I'm sure it's worth it!\n **(You gained {math.ceil(user['coins']/5)} coins**")
            await self.client.pg_con.execute("UPDATE users SET coins = $1 WHERE id=$2", user['coins'] + math.ceil(user['coins']/5), str(ctx.author.id))
        
def setup(client):
    client.add_cog(RR(client))
