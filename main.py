import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random

client = discord.Client()

words = ["♂️AH YES SIR♂️", "♂️FUCKING SLAVES GET YOUR ASS BACK HERE♂️", "♂️AAAAAAAAAAAAAAAAAAAH♂️", "♂️THANK YOU SIR♂️", "♂️LUKÁŠ JE PEDOFILNÍ WEEB♂️", "♂️OH MY SHOULDER♂️"]

@client.event
async def on_ready():
    print("Logged as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!billy"):
        while True:
            await message.channel.send(words[random.randint(0, 5)])
    if message.content.startswith("!wilson"):
         while True:
            await message.channel.send(":wilson:")
    if message.content.startswith("!penis"):
         await message.channel.send("8======D")  
    if message.content.startswith("heil"):
        while True:
            await message.channel.send("<:gachiHYPER:778672780773818389> ♂️ VŠECHNO NEJLEPŠÍ ONDŘEJI ♂️ <:gachiHYPER:778672780773818389>")

with open('Discord-bot\Token.txt') as f:
    Token = f.readline()
         
client.run(Token)


