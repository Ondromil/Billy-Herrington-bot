import discord
from discord.ext.commands import Bot
from discord.ext import commands
from MaxEmbeds import EmbedBuilder
import random

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')

@bot.event
async def on_ready():
    activity = discord.Game(name="Gachi |.help")
    await bot.change_presence(activity=activity)
    print("Logged as {0.user}".format(bot))

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if message.content.startswith("xd"):
        await message.channel.send("xd")
    if message.content.startswith("wilson"):
        await message.channel.send("wilson je absolutní gigachad")
    if message.content.startswith("fuck you"):
        await message.channel.send("ah fuck you leatherman")

@bot.event
async def on_member_remove(member):
     print(f"{member} leavnul muže :cry:")

@bot.command()
async def help(ctx):
    embed = EmbedBuilder(title="Help", description="**.billy** - Start Gachi Muchi rave").build()
    await ctx.send(embed=embed)

@bot.command()
async def billy(ctx):
    words = ["♂️AH YES SIR♂️", "♂️FUCKING SLAVES GET YOUR ASS BACK HERE♂️", "♂️AAAAAAAAAAAAAAAAAAAH♂️", "♂️THANK YOU SIR♂️", "♂️LUKÁŠ JE PEDOFILNÍ WEEB♂️", "♂️OH MY SHOULDER♂️"]
    for i in range(0, 50):
         await ctx.send(words[random.randint(0, 5)])

@bot.command()
async def enter(ctx):
    await ctx.send("Hey buddy I think you got the wrong door, the leather club is two blocks down")

with open('Discord-bot\.env') as f:
    Token = f.readline()

bot.run(Token)