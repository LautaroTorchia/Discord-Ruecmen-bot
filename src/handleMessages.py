from constants import *
import discord

async def handleMelMessage(m):
    if m.content.lower()==("mel"):
        await m.channel.send(MEL_MESSSAGE)
    
    if m.content.lower()==("mal"):
        await m.channel.send(MEL_MESSSAGE)


async def handleTecmanChange(m,client):
     if m.content.lower().startswith("$tecman"):
        with open(IMAGE_PATH, 'rb') as f:
            image = f.read()
            try:
                await client.user.edit(avatar=image,username="Tecman")
                await m.channel.send(TECMAN_APPEAR_MESSAGE)
            except discord.errors.HTTPException:
                await m.channel.send(TECMAN_ERROR_MESSAGE)


async def handleRecmanChange(m,client):
    if m.content.lower().startswith("$ruecman"):
        with open(IMAGE_PATH2, 'rb') as f:
            image = f.read()
            try:
                await client.user.edit(avatar=image,username="Ruecmen")
                await m.channel.send(RECMAN_APPEAR_MESSAGE)
            except discord.errors.HTTPException:
                await m.channel.send(RECMAN_ERROR_MESSAGE)
