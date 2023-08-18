import os
import json

import modules.helper as helper

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

INTENTS = discord.Intents.default()
INTENTS.message_content = True

bot = commands.Bot(command_prefix='$', intents=INTENTS)

@bot.command(name="scan")
async def scan(ctx):
    """ Checks if there's a new hacakthon

    Checks 'hackathons.json', gets list of upcoming hackathons
    using `helper.get_hackathons()` and compares the two. Then
    sends the hackathon links that are not in hackathons.json to
    the server.

    Args:
        ctx: A mandatory object-like argument for Discord API
    """    

    print(f'{bot.user} got an order to Scan.\n')

    try:
        # Open 'hackathons.json' file (if there is one)
        with open('hackathons.json', "r") as json_file:
            old_hackathons = json.load(json_file)
    except Exception as e:
        # If there is no 'hackathons.json' file created:
        old_hackathons = {}
    
    # Get the list of upcoming hackathons
    new_hackathons = helper.get_hackathons(helper.URL)

    if new_hackathons == old_hackathons:
        await ctx.send("No new Hackathons.")
    else:
        # Send the hackathons that are not in old_hackathons dict.
        for name in new_hackathons:
            if name not in old_hackathons:
                await ctx.send(new_hackathons[name])

bot.run(TOKEN)