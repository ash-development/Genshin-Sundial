# main.py
# @author : Chtholly2000
# @created : 2021-OCT-05 20:28
# @last updated: 2021-OCT-25 05:43

#Imports
import discord
import json
import os

from colorama import Fore
from discord.ext import commands
from discord.ext.commands import errors
from keep_alive import keep_alive

#Load Config
with open("config.json", "r") as config:
  data = json.load(config)
  prefix = data['prefix']

# ------------------------- BOT -------------------------- #
bot = commands.Bot(command_prefix= prefix , intents=discord.Intents.all())

#Remove Default Help Command
bot.remove_command("help")

@bot.event
async def on_ready():
  print(Fore.GREEN + f'Successfully logged in as {bot.user}')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{prefix}help"))

@bot.event
async def on_command_error(ctx,error):
  await ctx.send(f"__Error__ :\n```\n{str(error)}\n```")

#Custom Help Command
@bot.command()
async def help(ctx):
  embed = discord.Embed(title='__HELP__', description=f'```\n{prefix}servertime\n```Starts the __Server Time Embed__ and can only be used by the server owner', colour=0xFDD835)
  await ctx.send(embed=embed)
  
# --------------------- LOAD COGS ------------------------- #
for filename in os.listdir("./Cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"Cogs.{filename[:-3]}")
    print(Fore.BLUE+f"Successfully Loaded {filename}")

# -------------------------- RUN -------------------------- #
keep_alive()
token = os.getenv('token')
bot.run(token)