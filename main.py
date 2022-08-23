import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(
    "OTMzNzg1NDgwNjYxNzEyOTE2.G90GjM.Xeu19zGwwgGssJ2rJIzTTAuG7SQwP5Dj6Yyoic")
