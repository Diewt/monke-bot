import discord
import random
import os
import time
import requests

from db import DB

from torchvision import models, transforms
import torch
from PIL import Image

client = discord.Client()
db = DB()
resnet = models.resnet101(pretrained=True)
resnet.eval()

preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )])

#read in file of possible messages
with open("possible_messages.txt", "r") as files:
	possible_messages = files.readlines()

possible_messages = [i.strip('[]').replace('\n', '') for i in possible_messages]

def recognize_image(url):
    im = Image.open(requests.get(url, stream=True).raw).convert('RGB')
    img_t = preprocess(im)
    batch_t = torch.unsqueeze(img_t, 0)
    resnet.eval()
    out = resnet(batch_t)
    with open('imagenet_classes.txt') as f:
        labels = [line.strip() for line in f.readlines()]

    _, index = torch.max(out, 1)

    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
    animal = labels[index[0]].split(', ')[1]
    animal = animal.replace("_", ' ')
    im.close()

    return str("Me am " + str(int(percentage[index[0]].item())) + "% sure me see " + str(animal))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    num = random.randint(0, 100)

    #check if user exists, otherwise insert into database
    matching_users = db.getMatchingUserId(message.author.id)
    if matching_users.shape[0] == 0:
        db.createNewUserEntry(message.author.id)

    if message.content.lower().endswith(('jpeg', 'png', 'jpg')):
        recognize_str = recognize_image(message.content)
        await message.channel.send(recognize_str)
    elif message.attachments:
        for a in message.attachments:   
            recognize_str = recognize_image(a.url)
            await message.channel.send(recognize_str)

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
