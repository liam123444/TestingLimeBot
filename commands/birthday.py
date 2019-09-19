import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import datetime
import asyncpg 
#ok paps

class Bday(commands.Cog): 

    def __init__(self, client):
        self.client = client
    
    def paplooOrMe(ctx): 
        return ctx.author.id == 188373113166102528 or ctx.author.id == 348538644887240716
    
    @commands.command()
    @commands.check(paplooOrMe)
    async def addbday(self, ctx, person:discord.Member, bday): 
        bday = bday.split("-")
        await self.client.pg_con.execute("INSERT INTO bdays (id, bday) VALUES ($1, $2)", str(person.id), datetime.datetime(int(bday[0]), int(bday[1]), int(bday[2])))
        await ctx.send("Added!")
    
    @commands.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def bday(self, ctx):
        bdays = await self.client.pg_con.fetch("SELECT * FROM bdays")
        bdays = sorted(bdays, key=lambda bdays: bdays['bday'])
        if datetime.datetime.combine(bdays[0]['bday'], datetime.datetime.min.time()).strftime('%Y-%m-%d') < datetime.datetime.now().strftime('%Y-%m-%d'): 
            await self.client.pg_con.execute("UPDATE bdays SET bday = $1 WHERE id = $2", datetime.datetime(int(bdays[0]['bday'].strftime('%Y'))+1, int(bdays[0]['bday'].strftime('%m')), int(bdays[0]['bday'].strftime('%d'))), bdays[0]['id'])
            bdays = await self.client.pg_con.fetch("SELECT * FROM bdays")
            bdays = sorted(bdays, key=lambda bdays: bdays['bday'])
            
        
        if (datetime.datetime.combine(bdays[0]['bday'], datetime.datetime.min.time())-datetime.datetime.now()).days+1 == 0: 
            embed = discord.Embed(title="Birthday :tada:", description=f"It is <@!{bdays[0]['id']}>'s birthday today! Say happy birthday! :tada:")
        else: 
            embed = discord.Embed(title="Next Birthday", description=f"It will be <@!{bdays[0]['id']}>'s birthday in {(datetime.datetime.combine(bdays[0]['bday'], datetime.datetime.min.time())-datetime.datetime.now()).days+1} days")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.check(paplooOrMe)
    async def bedit(self, ctx, person:discord.Member, bday): 
        bday = bday.split("-")
        await self.client.pg_con.execute("UPDATE bdays SET bday = $1 WHERE id = $2", datetime.datetime(int(bday[0]), int(bday[1]), int(bday[2])), str(person.id))
        await ctx.send("Added!")
        
def setup(client):
    client.add_cog(Bday(client))
