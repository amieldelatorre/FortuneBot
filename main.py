import os
import discord 
import random

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()

TOKEN= os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!') # change how the bot is called here


def get_fortunes():
    file = open('fortunelist.txt', 'r')
    fortunes = file.readlines()
    return fortunes
    
fortunes = get_fortunes()



@bot.event
async def on_ready():
    print(
        f"FoodBot has connected to Discord!\n"
    )

@bot.command(name='fortune', help="This retrieves a fortune.")
async def get_fortune(context):
    fortune = random.choice(fortunes)
    print(f"Summoned from {context.guild}")
    await context.send(f"{context.author}'s fortune is...")
    await context.send(fortune)


bot.run(TOKEN)