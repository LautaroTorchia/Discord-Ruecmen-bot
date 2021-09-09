from logging import error
from constants import *
from discord.ext import commands
import discord


async def handleMelMessage(m):
    if m.content.lower()==("mel"):
        await m.channel.send(MEL_MESSSAGE)
    
    if m.content.lower()==("mal"):
        await m.channel.send(MEL_MESSSAGE)

async def handleTecmanChange(m,bot):
    with open(IMAGE_PATH, 'rb') as f:
        image = f.read()
        try:
            await bot.user.edit(avatar=image,username="Tecman")
            await m.channel.send(TECMAN_APPEAR_MESSAGE)
        except discord.errors.HTTPException:
            print(discord.errors.HTTPException)
            await m.channel.send(TECMAN_ERROR_MESSAGE)

async def handleRecmanChange(m,bot):
    with open(IMAGE_PATH2, 'rb') as f:
        image = f.read()
        try:
            await bot.user.edit(avatar=image,username="Recman")
            await m.channel.send(RECMAN_APPEAR_MESSAGE)
        except discord.errors.HTTPException:
            await m.channel.send(RECMAN_ERROR_MESSAGE)


