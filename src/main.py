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

@bot.command(name="tecman-punchi",help="TECMAN pone un temon")
async def punchiCommand(m):
    await handlePlay(m)

@bot.command(name="recman",help=RECMAN_HELP_TEXT)
async def recmanCommand(m):
    await handleRecmanChange(m,bot)

@bot.command(name="ono",help=ONO_HELP_TEXT)
async def onoCommand(m):
    await m.channel.send(f"{ONO_MESSAGE} "+"<@381907583687983107>")

@bot.command(name="match",help=MATCH_HISTORY_HELP_TEXT)
async def matchHistoryCommand(m,region,*args):
    await handleLolMatchHistory(m,region,*args)

@bot.command(name="summoner",help=SUMMONER_PROFILE_HELP_TEXT)
async def summonerProfileCommand(m,region,*args):
    await handleLolProfile(m,region,*args)

@bot.event
async def on_ready():
    print(f'we have logged in as {bot.user}')

@bot.event
async def on_message(m):
    if m.author==bot.user: #in case it tries to answer to himself
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


