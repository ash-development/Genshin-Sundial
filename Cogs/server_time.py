# ./Cogs/server_time.py
# @author : Chtholly2000
# @created : 2021-OCT-05 20:29
# @last updated : 2021-OCT-24 06:07

#Imports
import discord
import json
import pytz
import Utils.Function as function

from datetime import datetime
from discord.ext import tasks, commands
from discord.ext.commands import is_owner

# ---------------------- TIMEZONES --------------------- #
america = pytz.timezone('America/Cancun')
asia = pytz.timezone('Asia/Irkutsk')
europe = pytz.timezone('Africa/Algiers')

# ------------------------ COGS ------------------------ #
class ServerTime(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.server_time.start()
  
  def cog_unload(self):
    self.server_time.cancel()
# ------------------------------------------------------ #
    
  @tasks.loop(seconds=5.0)
  async def server_time(self):
    
    with open("config.json", "r") as config:
      data = json.load(config)
      CHANNEL_ID = data["CHANNEL_ID"]
      MESSAGE_ID = data["MESSAGE_ID"]
      GUILD_ID = data["GUILD_ID"]
      
    # --------------- AMERICAN SERVER -------------------- #
    America = (datetime.now(america).strftime("%H:%w:%M"))
    #Hours left
    Am_hour = int(America.split(':')[0])
    Am_hour_left_int = function.hour(Am_hour)
    Am_hour_left = str(Am_hour_left_int) + " " + function.sing_hour(Am_hour_left_int)
    #Minutes left
    Am_minute = int(America.split(':')[2])
    Am_minute_left_int = function.minute(Am_minute)
    Am_minute_left = str(Am_minute_left_int) + " " + function.sing_minute(Am_minute_left_int)
    #Days left
    Am_day = int(America.split(':')[1])
    Am_day_left_int = function.week(7 - Am_day)
    Am_day_left = str(Am_day_left_int) + " " + function.sing_day(Am_day_left_int)
    #Time now
    America_time = (datetime.now(america).strftime("%I:%M %p | %A"))
    
    # ---------------- EUROPEAN SERVER ------------------ #
    Europe = (datetime.now(europe).strftime("%H:%M:%w"))
    #Hours left
    Eu_hour = int(Europe.split(':')[0])
    Eu_hour_left_int = function.hour(Eu_hour)
    Eu_hour_left = str(Eu_hour_left_int) + " " + function.sing_hour(Eu_hour_left_int)
    #Minutes left
    Eu_minute = int(Europe.split(':')[1])
    Eu_minute_left_int = function.minute(Eu_minute)
    Eu_minute_left = str(Eu_minute_left_int) + " " + function.sing_minute(Eu_minute_left_int)
    #Days left
    Eu_day = int(Europe.split(':')[2])
    Eu_day_left_int = function.week(7 - Eu_day)
    Eu_day_left = str(Eu_day_left_int) + (" ") + function.sing_day(Eu_day_left_int)
    #Time Now
    Europe_time = (datetime.now(europe).strftime("%I:%M %p | %A"))
    
    # ----------------- ASIAN SERVER -------------------- #
    Asia = (datetime.now(asia).strftime("%H:%M:%w"))
    #Hours left
    As_hour = int(Asia.split(':')[0])
    As_hour_left_int = function.hour(As_hour)
    As_hour_left = str(As_hour_left_int) + " " + function.sing_hour(As_hour_left_int)
    #Minutes
    As_minute = int(Asia.split(':')[1])
    As_minute_left_int = function.minute(As_minute)
    As_minute_left = str(As_minute_left_int) + " " + function.sing_minute(As_minute_left_int)
    #Days left
    As_day = int(Asia.split(':')[2])
    As_day_left_int = function.week(7 - As_day)
    As_day_left = str(As_day_left_int) + " " + function.sing_day(As_day_left_int)
    #Time Now
    Asia_time = (datetime.now(asia).strftime("%I:%M %p | %A"))
    
    #No of users in Guild
    guild = self.bot.get_guild(GUILD_ID)
    u = guild.member_count
    users = function.comma(u)

    #Discord Embed
    embed = discord.Embed(description=f"**Server Status**\n\nMembers : {users}\n\n**Server Time:**\n```md\n# NA {America_time}\n```???Daily reset in {Am_hour_left} and {Am_minute_left}\n???Weekly reset in {Am_day_left}, {Am_hour_left} and {Am_minute_left}\n```\n# EU {Europe_time}\n```???Daily reset in {Eu_hour_left} and {Eu_minute_left}\n???Weekly reset in {Eu_day_left}, {Eu_hour_left} and {Eu_minute_left}\n```cs\n# Asia {Asia_time}\n```???Daily reset in {As_hour_left} and {As_minute_left}\n???Weekly reset in {As_day_left}, {As_hour_left} and {As_minute_left}\n```fix\n# SAR {Asia_time}\n```???Daily reset in {As_hour_left} and {As_minute_left}\n???Weekly reset in {As_day_left}, {As_hour_left}?? and {As_minute_left}\n\n[`Source Code`](https://github.com/Chtholly2000/Barbara)", colour=0x738ADB)
    embed.set_image(url="https://i.postimg.cc/kGYzvFx5/1148533.jpg")
    embed.set_footer(text="GENSHIN SERVER TIME")

    try:
      channel = self.bot.get_channel(CHANNEL_ID)
      message = await channel.fetch_message(MESSAGE_ID)
      await message.edit(embed=embed)
    except:
      self.server_time.cancel()
      
  @server_time.before_loop
  async def before_server_time(self):
    await self.bot.wait_until_ready()

    with open("config.json", "r") as config:
      data = json.load(config)
      
    try:
      channel = self.bot.get_channel(data['CHANNEL_ID'])
      message = await channel.fetch_message(data['MESSAGE_ID'])
    except:
      self.server_time.cancel()

  @commands.command()
  @is_owner()
  @commands.guild_only()
  async def servertime(self,ctx):
  
    await ctx.message.delete()
    message = await ctx.send(embed=discord.Embed(title='__SERVER TIME__', description = '???? If Embed is not editing itself, please open an issue [`here`](https://github.com/Chtholly2000/Barbara/issues)'))

    with open("config.json", "r") as config:
      data = json.load(config)
      data['MESSAGE_ID'] = message.id
      data['CHANNEL_ID'] = ctx.channel.id
      data['GUILD_ID'] = ctx.guild.id

    newdata = json.dumps(data, indent=4, ensure_ascii=False)

    with open("config.json", "w") as config:
      config.write(newdata)
    
    await self.server_time.start()
    
# ------------------------ BOT ------------------------ #
def setup(bot):
  bot.add_cog(ServerTime(bot))