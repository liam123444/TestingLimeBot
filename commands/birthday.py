import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import datetime
import asyncpg 
#ok

class Bday(commands.Cog): 

    def __init__(self, client):
        self.client = client
    
    def paplooOrMe(ctx): 
        return ctx.author.id == 188373113166102528 or ctx.author.id == 348538644887240716
    
    @commands.command()
    @commands.check(paplooOrMe)
    async def addbday(self, ctx, person:discord.Member, bday): 
        await self.client.pg_con.execute("INSERT INTO bdays (id, bday) VALUES ($1, $2)", str(person.id), bday)
        await ctx.send("Added!")
    
    @commands.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def bday(self, ctx):
        bdays = [
            [188373113166102528, datetime.datetime(2020, 9, 17), "Paploo"], 
            [171244585773826048, datetime.datetime(2020, 4, 28), "Yotta"], 
            [461593347316776960, datetime.datetime(2019, 10, 25), "JB"], 
            [241650038776791041, datetime.datetime(2020, 6, 25), "Jason"], 
            [252416555785256960, datetime.datetime(2019, 12, 9), "William"], 
            [282218272651345920, datetime.datetime(2019, 9, 23), "ssorsuper"], 
            [188344626543853568, datetime.datetime(2020, 7, 17), "scruffy"], 
            [417626694166249484, datetime.datetime(2020, 4, 16), "Chao"], 
            [234275916363202560, datetime.datetime(2020, 6, 25), "Dave"], 
            [191283118752268288, datetime.datetime(2020, 3, 29), "Eggs"]
        ]
        bdays = await self.client.pg_con.fetch("SELECT * FROM bdays")
        bdays = sorted(bdays, key=lambda bdays: bdays['bday'])
        if bdays[0][1].strftime("%x") < datetime.datetime.now().strftime("%x"): 
            bdays[0][1] = datetime.datetime(int(datetime.datetime.now().strftime("%Y"))+1, int(bdays[0][1].strftime("%m")), int(bdays[0][1].strftime("%d")))
            await self.client.pg_con.execute("UPDATE bdays SET bday = $1 WHERE bday = $2", f"{bdays[0][1].strftime('%Y')}-{bdays[0][1].strftime('%m')}-{bdays[0][1].strftime('%d')}", f"{int(bdays[0][1].strftime('%Y'))-1}-{bdays[0][1].strftime('%m')}-{bdays[0][1].strftime('%d')}")
            bdays = sorted(bdays, key=lambda bdays: bdays['bday'])
            
        
        if (bdays[0][1]-datetime.datetime.now()).days+1 == 0: 
            embed = discord.Embed(title="Birthday :tada:", description=f"It is <@{bdays[0][0]}>'s birthday today! Say happy birthday! :tada:")
        else: 
            embed = discord.Embed(title="Next Birthday", description=f"It will be <@{bdays[0][0]}>'s birthday in {(bdays[0][1]-datetime.datetime.now()).days+1} days")
        await ctx.send(embed=embed)

        
def setup(client):
    client.add_cog(Bday(client))
