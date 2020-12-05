import discord
import random

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    num = random.randint(0, 30)

    if message.author == client.user:
        return

    if num == 5:
        await message.channel.send('me monke')
    elif num == 6:
        await message.channel.send('no care, me monke')
    elif num == 7:
        await message.add_reaction(emoji='monkey')
    elif num == 8:
        await message.add_reaction(emoji='monkey_face')
    elif num == 9:
        await message.channel.send(':monkey:')
    elif num == 4:
        await message.channel.send(':monkey_face:')


client.run('Nzg0NjM5NzU3MzA0NzI1NTM0.X8sOuA.eyxrOiSH2kkjLEJFWoBPMoHKOOw')