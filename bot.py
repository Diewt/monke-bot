import discord
import random

client = discord.Client()
possible_messages = ['me monke', 'no care, me monke', ':monkey:', ':monkey_face:', "https://tenor.com/view/monkey-licking-tongue-french-gif-9316431", "https://tenor.com/view/obese-monkey-fat-monkey-summer-belly-eating-lettuce-summer-look-gif-13014350"]

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


client.run('Nzg0NjM5NzU3MzA0NzI1NTM0.X8sOuA.eyxrOiSH2kkjLEJFWoBPMoHKOOw')
