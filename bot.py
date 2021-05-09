import discord
import random
import os
import time

from db import DB

client = discord.Client()
db = DB()

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
    num2 = random.randint(0, 100000000)

    #check if user exists, otherwise insert into database
    matching_users = db.getMatchingUserId(message.author.id)
    if matching_users.shape[0] == 0:
        db.createNewUserEntry(message.author.id)

    if message.author == client.user:
        return

    if num2 == 69:
        await message.channel.send('https://giant.gfycat.com/SpottedUnconsciousGalapagostortoise.mp4')

    if num == 69:
        await message.channel.send(random.choice(possible_messages))
	
    if "pogchampion" in message.content.lower():
        await message.channel.send("Did you mean 'gopchampion'? Me monke.")
    elif "pogchamp" in message.content.lower():
        await message.channel.send("Did you mean 'gopchamp'? Me monke.")
    elif "pog" in message.content.lower():
        await message.channel.send("Did you mean 'gop'? Me monke.")
    elif "gop" in message.content.lower():
        await message.channel.send("Good job. You monke. Me monke.")
        
    if "based" in message.content.lower():
        based_str = message.content.lower().replace("based", "cringe")
        await message.channel.send(based_str)
    if "cringe" in message.content.lower():
        cringe_str = message.content.lower().replace("cringe", "based")
        await message.channel.send(cringe_str)

    if "monke" in message.content.lower():
        await message.channel.send("https://discord.com/oauth2/authorize?client_id=784639757304725534&scope=bot")


#placeholder for client joining voice channel


client.run(os.environ['DISCORD_BOT_TOKEN'])
