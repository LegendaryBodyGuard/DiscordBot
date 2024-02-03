# bot.py
import os
import discord
import random

from discord.ext import commands
from dotenv import load_dotenv

# from pyowm import OWM
# from pyowm.utils import config
# from pyowm.utils import timestamps

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
WEATHER = os.getenv('DISCORD_WEATHER')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
# client = discord.Client()


# @client.event
# async def on_ready():
#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break

#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})\n'
#     )

#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')

###############################################################################
#BELOW IS FOR THE BOT.                                                        #
#                                                                             #
###############################################################################

bot = commands.Bot(command_prefix='!',intents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# @bot.command(name='weather', help='Lets you know the weather')
# async def weather(ctx):
#     print("test")
#     await ctx.send(response)

###############################################################################
#DEMO NOT GOING TO BE PART OF FEATURE                                         #
#                                                                             #
###############################################################################
@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)
# client.run(TOKEN)