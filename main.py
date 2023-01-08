import os
import discord

my_token = os.environ['TOKEN']
intents = discord.Intents.default()
intents.message_content = True

image_types = ['png','jpeg','jpg']
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


#async def on_message(message: discord.Message):
  '''
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send("Hello!")
'''
@client.event
async def on_message(message: discord.Message):
    for attachment in message.attachments:
      if message.author == client.user:
        return
      if any(attachment.filename.lower().endswith(image) for image in image_types):
        await attachment.save(f'/home/runner/Ascii-New/{attachment.filename}')
        os.system(f'python ascii.py /home/runner/Ascii-New/{attachment.filename}')
        await message.channel.send(file=discord.File('/home/runner/Ascii-New/output.png'))
        os.remove(f'{attachment.filename}')
        os.remove('output.png')
client.run(my_token)