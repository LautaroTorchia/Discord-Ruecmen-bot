import os
from dotenv import load_dotenv
from discord.ext import commands
from constants import RECMAN_HELP_TEXT,TECMAN_HELP_MESSAGE
from handleMessages import *

load_dotenv()
bot = commands.Bot(command_prefix="$")

@bot.command(name="tecman",help=TECMAN_HELP_MESSAGE)
async def tecmanCommand(m):
    await handleTecmanChange(m,bot)


@bot.command(name="recman",help=RECMAN_HELP_TEXT)
async def recmanCommand(m):
    await handleRecmanChange(m,bot)

@bot.command(name="ono",help=ONO_HELP_TEXT)
async def onoCommand(m):
    await m.channel.send(f"{ONO_MESSAGE} "+"<@381907583687983107>")

@bot.command(name="mh",help=SUMMONER_HELP_TEXT)
async def matchHistoryCommand(m,region,summoner):
    print(region,summoner)
    await handleLolInfo(m,region,summoner)


@bot.event
async def on_ready():
    print(f'we have logged in as {bot.user}')

@bot.event
async def on_message(m):
    if m.author==bot.user:
        return

    await handleMelMessage(m)
    await bot.process_commands(m)
    
                           
@bot.event
async def on_member_join(member):
    guild=member.guild
    if guild.system_channel is not None:
        await guild.system_channel.send(f"Hola {guild.name} pa te saluda el ruecmen, diauer")


if __name__=="__main__":
    bot.run(os.getenv("TOKEN"))


