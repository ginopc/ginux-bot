import os
import discord
import requests
import json

# define constants
TOKEN = os.getenv('TOKEN')
QUOTE_PROVIDER_URL = os.getenv('QUOTE_PROVIDER_URL')

def get_quote():
  response = requests.get(QUOTE_PROVIDER_URL)
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' - by '  + json_data[0]['a']
  return(quote)

client = discord.Client()

@client.event
async def on_ready():
  print('Logger in as {0.user}'.format(client))

@client.event
async def on_message(message):
  # filter our message
  if (message.author == client.user):
    return

  if (message.content.startswith('hello')):
    await message.channel.send('Hello {0.author}'.format(message))

  if (message.content.startswith('$inspire')):
    quote = get_quote()
    await message.channel.send(quote)


# Run client
client.run(TOKEN)
