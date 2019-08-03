import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from discord.utils import get
import random
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
            if u == "None":
                await self.client.pg_con.execute("INSERT INTO users (id, coins, inventory) VALUES ($1, 0, '')", str(ctx.author.id))
            else:
                await self.client.pg_con.execute("INSERT INTO users (id, coins, inventory) VALUES ($1, 0, '')", str(u.id))
        
        if u == "None":
            user = await self.client.pg_con.fetchrow("SELECT * FROM users WHERE id = $1", str(ctx.author.id))
        else:
            user = await self.client.pg_con.fetchrow("SELECT * FROM users WHERE id = $1", str(u.id))
            
        await self.client.pg_con.execute("UPDATE users SET coins = $1 WHERE id=$2", user['coins'] + coins, user['id'])
        await ctx.send(f"{name} has been given {coins} coins!")

    @commands.command()
    async def coins(self, ctx, u:discord.Member = "None"):
        if u == "None":
            user = await self.client.pg_con.fetch("SELECT * FROM users WHERE id = $1", str(ctx.author.id))
        else:
            user = await self.client.pg_con.fetch("SELECT * FROM users WHERE id = $1", str(u.id))
            name = u.name
            
        if not user: 
            if u == "None":
                await self.client.pg_con.execute("INSERT INTO users (id, coins, inventory) VALUES ($1, 0, '')", str(ctx.author.id))
            else:
                await self.client.pg_con.execute("INSERT INTO users (id, coins, inventory) VALUES ($1, 0, '')", str(u.id))

        if u == "None":
            user = await self.client.pg_con.fetchrow("SELECT * FROM users WHERE id = $1", str(ctx.author.id))
        else:
            user = await self.client.pg_con.fetchrow("SELECT * FROM users WHERE id = $1", str(u.id))
        
        if u == "None":
            await ctx.send(f"You have {user['coins']} coins!")
        else: 
            await ctx.send(f"{name} has {user['coins']} coins!")         

    
    @commands.command()
    async def steal(self, ctx, u:discord.Member): 
        you = await self.client.pg_con.fetch("SELECT * FROM users WHERE id = $1", str(ctx.author.id))
        if not you:
            await ctx.send("You need atleast 1000 coins to use this command.")
            return
        if you[0]['coins'] < 1000:
            await ctx.send("You need atleast 1000 coins to use this command.")
            return             
        user = user = await self.client.pg_con.fetch("SELECT * FROM users WHERE id = $1", str(u.id))
        if not user:
            await ctx.send("The person you're stealing from needs atleast 1000 coins to rob from them.")
            return
        if user[0]['coins'] < 1000: 
            await ctx.send("The person you're stealing from needs atleast 1000 coins to rob from them.")
            return     
        
        rn = random.randint(0, 100)
        if rn < 80: 
            lose = random.randint(math.ceil(you[0]['coins']/6), math.ceil(you[0]['coins']/3))
            await ctx.send(f"{u.name} caught you trying to steal their coins! They demanded compensation so you paid {lose} to them.")
            await self.client.pg_con.execute("UPDATE users SET coins = $1 WHERE id=$2", you[0]['coins'] - lose, you[0]['id'])
            await self.client.pg_con.execute("UPDATE users SET coins = $1 WHERE id=$2", user[0]['coins'] + lose, user[0]['id'])
        else:
            win = random.randint(user[0]['coins']/8, user[0]['coins']/3)
            await ctx.send(f"You've made a new enemy! :smiling_imp: \nYou stole {win} from {u.name}")
            await self.client.pg_con.execute("UPDATE users SET coins = $1 WHERE id=$2", you[0]['coins'] + win, you[0]['id'])
            await self.client.pg_con.execute("UPDATE users SET coins = $1 WHERE id=$2", user[0]['coins'] - win, user[0]['id'])
       
        
def setup(client):
    client.add_cog(Coins(client))
