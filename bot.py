import discord
import random
import os

client = discord.Client()

#read in file of possible messages
with open("possible_messages.txt", "r") as files:
	possible_messages = files.readlines()

possible_messages = [i.strip('[]').replace('\n', '') for i in possible_messages]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    num = random.randint(0, 100)

    if message.author == client.user:
        return

    if num == 69:
        await message.channel.send(random.choice(possible_messages))
	
    if "monke" in str(message):
	for i in 10:
	    await message.channel.send("monke")

#placeholder for client joining voice channel


client.run(os.environ['DISCORD_BOT_TOKEN'])
