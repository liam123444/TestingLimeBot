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
            await ctx.send("You need coins to use this command.")
            return
        user = user[0]
        if user['coins'] == 0: 
            await ctx.send("You need coins to use this command.")
            return

        if random.randint(1, 5) == 3: 
            await ctx.send(f":gun: BANG! It was the bullet, I revived you but someone stole some of your coins while you were out.\n**(You lost {math.ceil(user['coins']/1.5)} coins)**")
            await self.client.pg_con.execute("UPDATE users SET coins = $1 WHERE id=$2", user['coins'] - random.randint(math.ceil(user['coins']/1.5), math.ceil(user['coins']/1.4)), str(ctx.author.id))    

        else:
            gain = random.randint(math.ceil(user['coins']/12), math.ceil(user['coins']/8))
            await ctx.send(f":gun: BANG! The gun shot out coins! It must hurt but I'm sure it's worth it!\n **(You gained {gain} coins)**")
            await self.client.pg_con.execute("UPDATE users SET coins = $1 WHERE id=$2", user['coins'] + gain, str(ctx.author.id))
        
def setup(client):
    client.add_cog(RR(client))
