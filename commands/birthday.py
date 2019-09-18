import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import datetime

class Bday(commands.Cog): 

    def __init__(self, client):
        self.client = client
            
    @commands.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def bday(self, ctx):
        bdays = [
            [188373113166102528, datetime.datetime(2020, 9, 17), "Paploo"], 
            [171244585773826048, datetime.datetime(2020, 4, 28), "Yotta"], 
            [461593347316776960, datetime.datetime(2019, 10, 25), "JB"], 
            [241650038776791041, datetime.datetime(2020, 6, 25), "Jason"], 
            [252416555785256960, datetime.datetime(2019, 12, 9), "William"], 
            [282218272651345920, datetime.datetime(2019, 9, 23), "ssorsuper"]
        ]
        bdays = sorted(bdays, key=lambda bdays: bdays[1])
        if bdays[0].strftime("%x") < datetime.datetime.strftime("%x"): 
            bdays[0][1] = datetime.datetime(int(datetime.datetime.now().strftime("%Y"))+1, int(bdays[0][1].strftime("%m")), int(bdays[0][1].strftime("%d")))
            bdays = sorted(bdays, key=lambda bdays: bdays[1])
        ctx.send(f"It is {bdays[0][2]}'s birthday in {(bdays[0][1]-datetime.datetime.now()).days+1} days")

        
def setup(client):
    client.add_cog(Bday(client))
