import cassiopeia
from cassiopeia.core.summoner import Summoner
import os
import discord
from constants import SUMMONER_NOT_FOUND_TEXT



async def handleLolMatchHistory(m,region,*args):
    name=" ".join(args)
    await m.channel.send("Ahi te la traigo pa")
    formated_data=""
    cassiopeia.set_riot_api_key(os.getenv("RIOT_API_KEY"))
    try:
        my_summoner=Summoner(name=name,region=region.upper())
        last_5=my_summoner.match_history[:5]
        games_data=list(map(lambda x:{"blue":x.blue_team,"red":x.red_team,"duration":x.duration,"id":x.id},last_5))
        games_data=list(map(lambda x:{"blue":x["blue"].participants,"red":x["red"].participants,"duration":x["duration"],"id":x["id"]},games_data))
        for i in games_data:
            red_team_data=""
            blue_team_data=""
            for x in i["red"]:
                red_team_data+=f"{x.summoner.name}({x.champion.name})  " 
            for x in i["blue"]:
                blue_team_data+=f"{x.summoner.name} ({x.champion.name})  "
            formated_data+=f"""

Blue side:  {blue_team_data} 

Red side: {red_team_data}  
 
 
duracion:{i["duration"]}  game_id:{i["id"]}

            """
        await m.channel.send(formated_data)
    except:
        await m.channel.send(SUMMONER_NOT_FOUND_TEXT)


async def handleLolProfile(m,region,*args):
    name=" ".join(args)
    try:
        my_summoner=Summoner(name=name,region=region.upper())
        embed=discord.Embed(title=my_summoner.name,color=discord.Color.blue(),
        url=f"https://{region}.op.gg/summoner/userName={name.replace(' ','+')}/",
        description="Este es el invocador que buscaste")
        await m.channel.send(embed=embed)
    except:
        await m.channel.send(SUMMONER_NOT_FOUND_TEXT)
