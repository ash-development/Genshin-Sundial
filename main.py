# main.py
# @author : Chtholly2000
# @created : 2021-OCT-05 20:28

#Imports
import os
import discord
import json

from discord.ext import commands
from discord.ext.commands import errors
from colorama import Fore
from keep_alive import keep_alive

bot = commands.Bot(command_prefix= '?' , intents=discord.Intents.all())

@bot.event
async def on_ready():
  print(Fore.GREEN + f'Successfully logged in as {bot.user}')

@bot.event
async def on_command_error(ctx,error):
  await ctx.send(f"__Error__ :\n```\n{str(error)}\n```") 
    
for filename in os.listdir("./Cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"Cogs.{filename[:-3]}")
    print(Fore.BLUE+f"Successfully Loaded {filename}")

keep_alive()
token=os.getenv('token')
bot.run(token)