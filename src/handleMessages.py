import cassiopeia
from constants import *
import discord
from cassiopeia import Summoner


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
    cassiopeia.set_riot_api_key("RGAPI-765777f5-0ec9-428a-9026-3f2b94c6378c")
    my_summoner=Summoner(name=summoner,region=region)
    print(my_summoner.account_id)
    print(type(my_summoner.match_history))
    campeones=my_summoner.match_history[0].blue_team
    jugadores=campeones.participants
    for i in jugadores:
        print(i.champion.name)

