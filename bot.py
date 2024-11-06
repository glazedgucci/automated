import discord
from discord.ext import tasks, commands
import asyncio

TOKEN = 'YOUR_BOT_TOKEN'
CHANNEL_ID = 123456789012345678  # Replace with your specific channel ID

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    scheduled_message.start()

@tasks.loop(hours=1)  # Runs every hour
async def scheduled_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        for i in range(10):  # Sends 10 messages
            await channel.send(f"This is message {i + 1} out of 10 for this hour.")
            await asyncio.sleep(1)  # Short delay between messages

# Error handling for commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That command doesn't exist.")

bot.run(TOKEN)