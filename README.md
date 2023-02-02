# ASCII-ify
This is a discord bot that converts images into ASCII art and sends the result in the form of both a .txt and .png file. The bot is triggered when an image is sent to a specific channel in a discord server.
# Requirements
- Replit account
- Discord Developer account
# Setup
1. Set up a Discord bot and obtain a token for it: https://discord.com/developers/docs/getting-started#creating-an-app
2. Invite the bot to your server
3. Create a replit account then head to https://replit.com/@bdakhel/ASCII-ify and fork repl
4. Enter the channel-id you'd like the bot to operate in and Discord API key as secrets in the repl project
5. Run code
6. Send an image to the specified channel-id
# How it Works
The bot listens in the specified channel for image attachments. When a message containing an image is detected, the bot saves the image, ASCII-ifies it, and sends the ASCII art in both .txt and .png format to the same channel.
