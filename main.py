import discord
from discord.ext.commands import Bot
from discord.ext import commands
from MaxEmbeds import EmbedBuilder
import random

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')                 # removes help base command, so it can be replaced by bots help command

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
    helpEmbed = EmbedBuilder(title="Help", description="Command menu").build()
    helpEmbed.add_field(name=".billy", value="Start Gachi Muchi rave", inline=False)
    helpEmbed.add_field(name=".enter", value="Enter the Lockerooms", inline=False)
    helpEmbed.add_field(name=".wrestle", value="Start wrestling (minigame)", inline=False)
    helpEmbed.add_field(name=".ping", value="Shows bot's latency", inline=False)
    await ctx.send(embed=helpEmbed)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! :ping_pong:   {0} ms".format(round(bot.latency * 1000)))

@bot.command()
async def billy(ctx):
    global words
    words = ["♂️AH YES SIR♂️", "♂️FUCKING SLAVES GET YOUR ASS BACK HERE♂️", "♂️AAAAAAAAAAAAAAAAAAAH♂️", "♂️THANK YOU SIR♂️", "♂️LUKÁŠ JE PEDOFILNÍ WEEB♂️", "♂️OH MY SHOULDER♂️"]
    for i in range(0, 50):
         await ctx.send(words[random.randint(0, 5)])

@bot.command()
async def enter(ctx):
    await ctx.send("Hey buddy I think you got the wrong door, the leather club is two blocks down")

isFighting = False
@bot.command()
async def wrestle(ctx):
    global isFighting
    if isFighting == False:
        global playerHealth
        playerHealth = 100
        global enemyHealth
        enemyHealth = 100 
        isFighting = True
        embeds()
        await ctx.send(embed=fightEmbed)
        await ctx.send(embed=selectionEmbed)
    else:
        await ctx.send("You are already wrestling")

@bot.command()
async def a(ctx):
    global isFighting
    if isFighting == True:
        global enemyHealth
        global playerHealth
        damageDoneToEnemy = random.randrange(5, 15)
        damageDoneToPlayer = random.randrange(5, 15)
        enemyHealth -= damageDoneToEnemy
        await ctx.send(random.choice(words))
        await ctx.send("You did {0} damage".format(damageDoneToEnemy))
        if (enemyHealth <= 0):
            await ctx.send("You won! :partying_face:")
            isFighting = False
        else:
            playerHealth -= damageDoneToPlayer
            await ctx.send("You took {0} damage".format(damageDoneToPlayer))
        if (playerHealth <= 0):
            await ctx.send("You lost! :cry:")
            isFighting = False
        if isFighting == True:
            embeds()
            await ctx.send(embed=fightEmbed)         
    else:
        await ctx.send("You are not wrestling")

@bot.command()
async def h(ctx):
    global isFighting
    if isFighting == True:
        global playerHealth
        global enemyHealth
        healthHealed = random.randrange(5, 15)
        damageDoneToPlayer = random.randrange(5, 15)
        playerHealth += healthHealed
        await ctx.send(random.choice(words))
        await ctx.send("You have healed {0} health".format(healthHealed))
        playerHealth -= damageDoneToPlayer
        await ctx.send("You took {0} damage".format(damageDoneToPlayer))
        if (playerHealth <= 0):
            await ctx.send("You lost! :cry:")
            isFighting = False
        if isFighting == True:
            embeds()
            await ctx.send(embed=fightEmbed)         
    else:
        await ctx.send("You are not wrestling")

@bot.command()
async def s(ctx):
    global isFighting
    if isFighting == True:
        await ctx.send("You have surrendered :flag_fr:")
        isFighting = False
    else:
        await ctx.send("You are not even fighting and already want to surrender, fucking frenchie")

@bot.command()
async def t(ctx):
    embeds()
    await ctx.send(embed=selectionEmbed)
 
words = ["♂️AH YES SIR♂️", "♂️FUCKING SLAVES GET YOUR ASS BACK HERE♂️", "♂️AAAAAAAAAAAAAAAAAAAH♂️", "♂️THANK YOU SIR♂️", "♂️LUKÁŠ JE PEDOFILNÍ WEEB♂️", "♂️OH MY SHOULDER♂️"]   

def embeds():
     global fightEmbed
     global selectionEmbed
     fightEmbed = EmbedBuilder(title="Battle", description="---------------------").build()
     fightEmbed.add_field(name="Billy Herrington",value="Health: {0}".format(enemyHealth), inline=False)
     fightEmbed.add_field(name="Van Darkholme (You)", value="Health: {0}".format(playerHealth), inline=False)
     selectionEmbed = EmbedBuilder(title="Tutorial", description="Commands for wrestling minigame").build()
     selectionEmbed.add_field(name=".a", value="Attack, deals between 5-15 damage", inline=False)
     selectionEmbed.add_field(name=".h", value="Heal, heals between 5-15 hp", inline=False)
     selectionEmbed.add_field(name=".s", value="Surrender", inline=False)
     selectionEmbed.add_field(name=".t", value="Diplay tutorial again", inline=False)
     
with open('Discord-bot\.env') as f:
    Token = f.readline()

bot.run(Token)