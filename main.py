
import discord
from discord.ext import commands
from sys import prefix

client = discord.Client()
bot = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("hello")

