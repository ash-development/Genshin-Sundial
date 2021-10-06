
#Imports
import discord
import requests
import DiscordUtils

from discord.ext import commands
from Utils.Function import Element

class Characters(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  
  @commands.command(aliases=['chr'])
  async def character (self, ctx, *, character: str):
    character = character.replace("'", "-")
    character = character.replace(" ", "-")
    url = f"https://api.genshin.dev/characters/{character}"
    stats = requests.get(url)
    json_stats = stats.json()
    
    if 'error' not in json_stats:
      stars = ''
      for i in range(json_stats['rarity']):
        stars += '⭐'
      name = json_stats["name"]
      desc = json_stats["description"]
      rarity = stars
      vision = json_stats["vision"]
      weapon = json_stats["weapon"]
      nation = json_stats["nation"]
      affiliation = json_stats["affiliation"]
      constellation = json_stats["constellation"]
      birthday = json_stats["birthday"].split('-')
      Birthday = birthday[1] + '/' + birthday[2]
      cons = json_stats["constellations"]
      passive = json_stats["passiveTalents"]
      element = json_stats["vision"].lower()

      talent = json_stats["skillTalents"]
      Normal_Name = talent[0]['name']
      Normal_Description = talent[0]['description']
      Elemental_Name = talent[1]['name']
      Elemental_Description = talent[1]['description']
      Brust_Name = talent[2]['name']
      Brust_Description = talent[2]['description']

      #Embed 1 - General Info
      embed1 = discord.Embed(title=f'__{name}__', description=desc, colour=Element(vision))
      embed1.set_thumbnail(url=f"https://api.genshin.dev/elements/{element}/icon")
      embed1.add_field(name='__Rarity__', value=f'{rarity}', inline=True)
      embed1.add_field(name='__Vision__', value=vision, inline=True)
      embed1.add_field(name='__Weapon__', value=weapon, inline=True)
      embed1.add_field(name='__Nation__', value=nation, inline=True)
      embed1.add_field(name='__Affiliation__', value=affiliation, inline=True)
      embed1.add_field(name='__Constellation__', value=constellation, inline=True)
      embed1.add_field(name='__Birthday__', value=Birthday, inline=True)
      embed1.set_image(url=f"https://api.genshin.dev/characters/{character}/gacha-splash")
    
      #Embed 2 - Constellations
      embed2 = discord.Embed(title="__Constellations__", colour=Element(vision))
      embed2.set_thumbnail(url=f"https://api.genshin.dev/characters/{character}/icon")
      for constel in cons:
        embed2.add_field(name="__                                                          __", value="```CSS\n[{}]\n{}```\n```\n{}\n```".format(constel['name'],constel['unlock'],constel['description']), inline=False)

      #Embed 3 - Talents 
      embed3 = discord.Embed(title="__Talents__", description=f'```FIX\n[{Normal_Name}]\nNormal Attack\n```\n```\n{Normal_Description}\n```\n```FIX\n[{Elemental_Name}]\nElemental Skill\n```\n```\n{Elemental_Description}\n```\n```FIX\n[{Brust_Name}]\nElemental Brust\n```\n```\n{Brust_Description}\n```', colour = Element(vision))
      embed3.set_thumbnail(url=f"https://api.genshin.dev/characters/{character}/icon")

      #Embed 4 - Passives 
      embed4 = discord.Embed(title="__Passives__", colour = Element(vision))
      embed4.set_thumbnail(url=f"https://api.genshin.dev/characters/{character}/icon")
      for pasif in passive:
        embed4.add_field(name="__                                                          __", value="```FIX\n[{}]\n{}```\n```\n{}\n```\n".format(pasif['name'],pasif['unlock'],pasif['description']), inline=False)

      #Paginator
      paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
      paginator.add_reaction('⏪', "back")
      paginator.add_reaction('⏩', "next")
      embeds = [embed1, embed2, embed3, embed4]
      await paginator.run(embeds)  

    else: 
      await ctx.send(f"```\n{json_stats['error']}\n```")  
  
  @commands.command(aliases=['charalist'])   
  async def characters(self, ctx):
    url = f"https://api.genshin.dev/characters"
    stats = requests.get(url)
    charas = stats.json()
    embed = discord.Embed(title="Character list", description="```"+"\n".join(charas)+"```", color=discord.Color.orange())
    embed.set_footer(text="use `+character <chara name>`")
    
    await ctx.author.send(embed=embed)
    await ctx.send("I sent you the character list on your DM!")
    
def setup(bot):
  bot.add_cog(Characters(bot))