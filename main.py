import discord
from discord.ext.commands import Bot
from discord.ext import commands
from MaxEmbeds import EmbedBuilder
import random

bot = commands.Bot(command_prefix='!')

bot.remove_command('help')
@bot.event
async def on_ready():
    activity = discord.Game(name="Sex with Hitler")
    await bot.change_presence(activity=activity)
    print("Logged as {0.user}".format(bot))

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if message.content.startswith("xd"):
        await message.channel.send("xd")

@bot.event
async def on_member_remove(member):
     await message.channel.send(f"{member} leavnul muže :cry:")

@bot.command()
async def help(ctx):
    embed = EmbedBuilder(title="Help", description="**!billy** - Start Gachi Muchi rave").build()
    await ctx.send(embed=embed)

@bot.command()
async def billy(ctx):
    words = ["♂️AH YES SIR♂️", "♂️FUCKING SLAVES GET YOUR ASS BACK HERE♂️", "♂️AAAAAAAAAAAAAAAAAAAH♂️", "♂️THANK YOU SIR♂️", "♂️LUKÁŠ JE PEDOFILNÍ WEEB♂️", "♂️OH MY SHOULDER♂️"]
    for i in range(0, 50):
         await ctx.send(words[random.randint(0, 5)])

with open('Discord-bot\.env') as f:
    Token = f.readline()

bot.run(Token)