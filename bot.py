import discord
import random
import os
import time

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
	
    if "monke" in str(message) and (message.author != client.user) and ("mine" in str(message.channel)):
        print("monke detected")
        time.sleep(1)
        for i in range(10):
            await message.channel.send("monke")

#placeholder for client joining voice channel


client.run(os.environ['DISCORD_BOT_TOKEN'])
