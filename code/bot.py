# bot.py
import os
import discord
import random
import pyowm

from discord.ext import commands
from dotenv import load_dotenv

# Weather Bots api
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
WEATHER = pyowm.OWM(os.getenv('DISCORD_WEATHER'))


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

@bot.command(name='weather', help='Lets you know the weather. usage example city,State')
async def getweatherInfo(ctx,location):
    mgr = WEATHER.weather_manager()
    observation = mgr.weather_at_place(location)
    # observation = mgr.weather_at_place('London,GB')
    w = observation.weather

    # w.detailed_status,         # 'clouds'
    # w.wind(),                  # {'speed': 4.6, 'deg': 330}
    # w.humidity,                # 87
    # w.temperature('celsius'),  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    # w.rain,                    # {}
    # w.heat_index,              # None
    # w.clouds                  # 75
    # w.weather
    temp = w.temperature(unit='fahrenheit')
    status = w.detailed_status

    await ctx.send(f"The weather in {location} is " + str(int(temp['temp'])) + " degrees and " + status)
    # Will it be clear tomorrow at this time in Milan (Italy) ?
    # forecast = mgr.forecast_at_place('Milan,IT', 'daily')
    # answer = forecast.will_be_clear_at(timestamps.tomorrow())

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