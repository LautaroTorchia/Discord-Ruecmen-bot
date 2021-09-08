import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

from handleMessages import handleMelMessage, handleRecmanChange, handleTecmanChange

load_dotenv()


#bot = commands.Bot(command_prefix="$")
client= discord.Client()


@client.event
async def on_ready():
    print(f'we have logged in as {client.user}')

@client.event
async def on_message(m):
    if m.author==client.user:
        return

    await handleMelMessage(m)
    await handleTecmanChange(m,client)
    await handleRecmanChange(m,client)
           
    
                
@client.event
async def on_member_join(self,member):
    guild=member.guild
    if guild.system_channel is not None:
        await guild.system_channel.send(f"Hola {guild.name} pa te saluda el ruecmen, diauer")

if __name__=="__main__":
    client.run(os.getenv("TOKEN"))


