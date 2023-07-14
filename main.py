import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')

@bot.command()
async def organic(ctx):
    with open('organic.txt', 'r', encoding='UTF-8') as f:
        file_content = f.read()
        f.close()

    await ctx.send(file_content)

@bot.command()
async def inorganic(ctx):
    with open('inorganic.txt', 'r', encoding='UTF-8') as f:
        file_content = f.read()
        f.close()

    await ctx.send(file_content)

bot.run('')       