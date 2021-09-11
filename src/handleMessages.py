import asyncio
from constants import *
import discord
from dotenv import load_dotenv

load_dotenv() #For the token


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

async def handleJubiladitaMessage(m):
    await m.channel.send(JUBILADITA_MESSAGE)
            

async def handlePlay(ctx):
    if not ctx.message.author.voice:
        await ctx.send('Tengo que meterme al canal primero locoooo')
        return
    else:
        channel = ctx.message.author.voice.channel
    voice_client = await channel.connect()
    guild = ctx.message.guild
    path =MUSIC_PATH1
    voice_client.play(discord.FFmpegPCMAudio(path))
    voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)
    await ctx.send(f'**Music: ** Nightcore- Highscore')

    while voice_client.is_playing():
        await asyncio.sleep(1)
    else:
        await voice_client.disconnect()
        await ctx.channel.send(TECMAN_LEAVES_VOICE_CHAT_TEXT)


