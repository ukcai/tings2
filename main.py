import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check     
import webserver
import urllib
import json


client = discord.Client()

client = commands.Bot(command_prefix = '!') #put your own prefix here

@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online

@client.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx,member : discord.Member,*,reason="no reason given"):
  if member == ctx.author:
    await ctx.send("you cant warn yourself")
  else:
    em = discord.Embed(title="**warned**", description=f"{member} was warned because {reason}", color=discord.Color.red())
    em2 = discord.Embed(title="**warned**", description=f"you were warned because {reason}", color=discord.Color.red())
    await member.send(embed=em2)
    await ctx.send(embed=em)
    

@client.command()
async def meme(ctx):
  memeApi = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')

  memeData = json.load(memeApi)

  memeUrl =memeData['url']
  memeName = memeData['title']
  memePoster = memeData['author']
  memeLink = memeData['postLink']

  embed = discord.Embed(title=memeName)
  embed.set_image(url=memeUrl)
  embed.set_footer(text=f"meme by {memePoster}")
  await ctx.send(embed=embed)
  
    
    
@client.command()
async def ping(ctx):
    await ctx.send("pong!") #simple command so that when you type "!ping" the bot will respond with "pong!"
@client.command()
async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")

@client.command()
async def hi(ctx):
  await ctx.send("hi!")

client.run(os.getenv("TOKEN")) #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!

