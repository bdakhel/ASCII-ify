import os
import discord

# Assign token from replit secrets
my_token = os.environ['TOKEN']

# Allow bot to view message content
intents = discord.Intents.default()
intents.message_content = True

# Create instance of client
client = discord.Client(intents=intents)

# Notify of secure connection
@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message: discord.Message):
  # Setup Channel id
  channel_id = '1061409366621814809'
  # Do not ASCII-ify Images sent by bot
  if message.author == client.user:
        return
  # If image is sent is channel set up
  if str(message.channel.id) == channel_id:
    # Loop through attachments
    for attachment in message.attachments:
      # If an image
      image_types = ['png','jpeg','jpg']
      if any(attachment.filename.lower().endswith(image) for image in image_types):
        # Save image
        await attachment.save(f'/home/runner/ASCII-ify/{attachment.filename}')
        # ASCII-ify
        os.system(f'python ascii.py /home/runner/ASCII-ify/{attachment.filename}')
        # Send png file
        await message.channel.send(file=discord.File(f'/home/runner/ASCII-ify/ASCII-ified.png'))
        # Send txt file
        await message.channel.send(file=discord.File(f'/home/runner/ASCII-ify/ASCII-ified.txt'))
        # Remove saved images
        os.remove('ASCII-ified.png')
        os.remove('ASCII-ified.txt')
        os.remove(f'{attachment.filename}')
client.run(my_token)
