import discord
import random
import os
import time
import requests
import json

from db import DB

from torchvision import models, transforms
import torch
from PIL import Image

client = discord.Client()
db = DB()
model = models.densenet121(pretrained=True)
model.eval()

preprocess = transforms.Compose([
        transforms.Resize(255),
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
    imagenet_class_index = json.load(open('imagenet_class_index.json'))
    im = Image.open(requests.get(url, stream=True).raw).convert('RGB')
    tensor = preprocess(im).unsqueeze(0)
    im.close()
    outputs = model.forward(tensor)

    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    prediction = imagenet_class_index[predicted_idx][1].replace('_', ' ').lower()
    if prediction == "comic book":
        meme_choice = ["good meme", "bad meme"]
        return meme_choice[random.choice([0,1])]
    else:
        return prediction

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
        recognized_animal = recognize_image(message.content)
        await message.channel.send("Me thinks me see " + recognized_animal)
    elif message.attachments:
        for a in message.attachments:   
            recognized_animal = recognize_image(a.url)
            await message.channel.send("Me thinks me see " + recognized_animal)

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

    if "photo" in message.content.lower():
        if num < 50:
            await message.channel.send("bogos binted?")
        else:
            await message.channel.send("dogos dinted?")

    if "monke" in message.content.lower():
        await message.channel.send("https://discord.com/oauth2/authorize?client_id=784639757304725534&scope=bot")


#placeholder for client joining voice channel


client.run(os.environ['DISCORD_BOT_TOKEN'])
