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
    cassiopeia.set_riot_api_key(os.getenv("RIOT_API_KEY"))
    my_summoner=Summoner(name=summoner,region=region)
    ultimas5=my_summoner.match_history[:5]
    print(ultimas5)


