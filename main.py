import os
import discord

TOKEN=os.getenv('TOKEN')

client=discord.Client()

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

client.run(TOKEN)

