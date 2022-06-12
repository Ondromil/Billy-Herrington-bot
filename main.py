import discord
from discord.ext.commands import Bot
from discord.ext import commands
from MaxEmbeds import EmbedBuilder
import random

client = discord.Client()

words = ["♂️AH YES SIR♂️", "♂️FUCKING SLAVES GET YOUR ASS BACK HERE♂️", "♂️AAAAAAAAAAAAAAAAAAAH♂️", "♂️THANK YOU SIR♂️", "♂️LUKÁŠ JE PEDOFILNÍ WEEB♂️", "♂️OH MY SHOULDER♂️"]

@client.event
async def on_ready():
    activity = discord.Game(name="Sex with Hitler")
    await client.change_presence(activity=activity)
    print("Logged as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!billy"):
        for i in range(0, 50):
             await message.channel.send(words[random.randint(0, 5)])
    if message.content.startswith("!help"):
        embed = EmbedBuilder(title="Help", description="**!billy** - Start Gachi Muchi rave").build()
        await message.channel.send(embed=embed)
    if message.content.startswith("xd"):
        await message.channel.send("xd")

with open('Discord-bot\Token.env') as f:
    Token = f.readline()

client.run(Token)