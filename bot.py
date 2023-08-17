import os
import json

import modules.helper as helper

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

INTENTS = discord.Intents.default()
INTENTS.message_content = True

bot = commands.Bot(command_prefix='$', intents=INTENTS)

@bot.command(name="scan")
async def scan(ctx):
    print(f'{bot.user} got an order to Scan.\n')

    try:
        with open('hackathons.json', "r") as json_file:
            old_hackathons = json.load(json_file)
    except Exception as e:
        old_hackathons = {}
    
    new_hackathons = helper.get_hackathons(helper.URL)

    if new_hackathons == old_hackathons:
        await ctx.send("No new Hackathons.")
    else:
        for name in new_hackathons:
            if name not in old_hackathons:
                await ctx.send(new_hackathons[name])

bot.run(TOKEN)