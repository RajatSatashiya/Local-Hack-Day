import os
import discord
import random
import requests
import json

client = discord.Client()

def get_joke():
  response = requests.get("https://api.icndb.com/jokes/random")
  json_data = json.loads(response.text)
  joke = json_data['value']['joke']
  return joke

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -"+json_data[0]['a']
  return quote


@client.event
async def on_ready():
  print('Logged in as : {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('/hello'):
    await message.channel.send('Rebek! Rebek !!')

  if message.content.startswith('/give-me-title'):
    titles=["Evil King","Monster Swag","Frog-Lover","Elephant-Heart", "Lunch Money Splern"]
    n = random.randint(0,4)
    await message.channel.send(titles[n])
    
  if message.content.startswith('/quote'):
    await message.channel.send(get_quote())

    
  if message.content.startswith('/joke'):
    joke = get_joke()
    await message.channel.send(joke)
  
  if message.content.startswith('/rebek'):
    await message.channel.send("Here's a list of commands: \n/hello \n/give-me-title \n/quote \n/joke :)")


my_secret = os.environ['TOKEN']
client.run(my_secret)


