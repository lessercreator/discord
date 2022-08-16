#bot.py
import os
import discord
import random

TOKEN = 'OTM1NTkyMDc4MzcxNjA2NTQ4.YfA4BQ.QloSLhBmgNJTSiNPGAUCTppCbz4'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    announce = []
    triggers = []

    if (message.content).lower() in triggers:
        response = random.choice(announce)
        await message.channel.send(response)

client.run(TOKEN)
