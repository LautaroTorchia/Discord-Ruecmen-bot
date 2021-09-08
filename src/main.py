import discord
import os
from dotenv import load_dotenv

load_dotenv()

IMAGE_PATH="src/Foto1.jpg"
IMAGE_PATH2="src/Foto2.png"

client= discord.Client()

@client.event
async def on_ready():
    print(f'we have logged in as {client.user}')

@client.event
async def on_message(m):
    if m.author==client.user:
        return
    if m.content.upper()==("MEL"):
        await m.channel.send("MEEEEEEEEEEEEEEEEEEEEEEEEEEL")
    
    if m.content.upper()==("MAL"):
        await m.channel.send("MEEEEEEEEEEEEEEEEEEEEEEEEEEL")
    
    if m.content.upper().startswith("$TECMAN"):
        with open(IMAGE_PATH, 'rb') as f:
            image = f.read()
            try:
                await client.user.edit(avatar=image,username="Tecman")
                await m.channel.send("ESTOY EN MI FORMA FINAL")
            except discord.errors.HTTPException:
                await m.channel.send("TECMAN NO ESTA LISTO AUN(Ocurrio un error al cambiar)")
        
    if m.content.upper().startswith("$RUECMEN"):
        with open(IMAGE_PATH2, 'rb') as f:
            image = f.read()
            try:
                await client.user.edit(avatar=image,username="Ruecmen")
                await m.channel.send("Volvi a la normalidad")
            except discord.errors.HTTPException:
                await m.channel.send("No estoy preparado para volver(Ocurrio un error al cambiar)")
                
@client.event
async def on_member_join(self,member):
    guild=member.guild
    if guild.system_channel is not None:
        await guild.system_channel.send(f"Hola {guild.name} pa te saluda el ruecmen, diauer")

client.run(os.getenv("TOKEN"))


