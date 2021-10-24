# main.py
# @author : Chtholly2000
# @created : 2021-OCT-05 20:28
# @last updated: 2021-OCT-24 23:17

#Imports
import discord
import json
import os

from colorama import Fore
from discord.ext import commands
from discord.ext.commands import errors
from keep_alive import keep_alive

# ------------------------- BOT -------------------------- #
bot = commands.Bot(command_prefix= '?' , intents=discord.Intents.all())

@bot.event
async def on_ready():
  print(Fore.GREEN + f'Successfully logged in as {bot.user}')

@bot.event
async def on_command_error(ctx,error):
  await ctx.send(f"__Error__ :\n```\n{str(error)}\n```") 

# --------------------- LOAD COGS ------------------------- #
for filename in os.listdir("./Cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"Cogs.{filename[:-3]}")
    print(Fore.BLUE+f"Successfully Loaded {filename}")

# -------------------------- RUN -------------------------- #
try:
  keep_alive()
  token = os.getenv('token')
  bot.run(token)
except:
  print(Fore.RED+'Add token as Environmental Variable')