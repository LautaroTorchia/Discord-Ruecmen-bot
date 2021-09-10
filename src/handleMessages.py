import os
import cassiopeia
from constants import *
import discord
from dotenv import load_dotenv
from cassiopeia import Summoner

load_dotenv()

async def handleMelMessage(m):
    if m.content.lower()==("mel") or m.content.lower()==("mal"):
        await m.channel.send(MEL_MESSSAGE)


async def handleTecmanChange(m,bot):
    with open(IMAGE_PATH, 'rb') as f:
        image = f.read()
        try:
            await bot.user.edit(avatar=image,username="Tecman")
            await m.channel.send(TECMAN_APPEAR_MESSAGE)
        except discord.errors.HTTPException:
            await m.channel.send(TECMAN_ERROR_MESSAGE)

async def handleRecmanChange(m,bot):
    with open(IMAGE_PATH2, 'rb') as f:
        image = f.read()
        try:
            await bot.user.edit(avatar=image,username="Recman")
            await m.channel.send(RECMAN_APPEAR_MESSAGE)
        except discord.errors.HTTPException:
            await m.channel.send(RECMAN_ERROR_MESSAGE)
            

async def handleLolInfo(m,region,summoner):
    
    formated_data=""

    cassiopeia.set_riot_api_key(os.getenv("RIOT_API_KEY"))
    my_summoner=Summoner(name=summoner,region=region)
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
Blue side: {blue_team_data} 

Red side: {red_team_data}  

duracion:{i["duration"]}  game_id:{i["id"]}

        """
    await m.channel.send(formated_data)
    


