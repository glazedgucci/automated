import discord
from discord.ext import tasks, commands
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))  # Convert to int for channel ID

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    scheduled_message.start()  # Start the scheduled task when the bot is ready

@tasks.loop(hours=1)  # Runs every hour
async def scheduled_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        for i in range(10):  # Sends 10 messages
            await channel.send(f"This is message {i + 1} out of 10 for this hour.")
            await asyncio.sleep(1)  # Short delay between messages to prevent flooding

# Run the bot
bot.run(TOKEN)