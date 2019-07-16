import discord
from discord.ext import commands
from discord.utils import get
import os
import random 

client = commands.Bot(command_prefix=";", case_insensitive=True)

status = "How to train your dragon"

emotes = ["1", "2", "3", "4", "5"]
role = [350314217879896066, 423253740246794241, 310784232093908992, 316977167298985985, 545737840697278464]

@client.event
async def on_ready():
    print("The bot is ready")
    await client.change_presence(activity=discord.Activity(name=status, type=discord.ActivityType.watching))

@client.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == 600343727516680205 and payload.message_id == 600343767739924481: 
        server = get(client.guilds, id=payload.guild_id)
        user = get(server.members, id=payload.user_id)
        getRole = get(server.roles, id=role[emotes.index(str(payload.emoji.name)[:1])])
        await user.add_roles(getRole)

@client.command()
@commands.is_owner()
async def load(ctx, extenstion):
    client.load_extension(f'commands.{extenstion}')

@client.command()
@commands.is_owner()
async def unload(ctx, extenstion):
    client.unload_extension(f'commands.{extenstion}')

@client.command()
@commands.is_owner()
async def reload(ctx, extenstion):
    client.unload_extension(f'commands.{extenstion}')
    client.load_extension(f'commands.{extenstion}')

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')

client.run(os.getenv('TOKEN'))