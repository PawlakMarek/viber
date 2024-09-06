import os

import discord
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Access the token from the environment variables
TOKEN = str(os.getenv("DISCORD_BOT_TOKEN"))


class ViberBot(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return
        else:
            print(f"Message from {message.author}: {message.content}")


intents = discord.Intents.default()
intents.message_content = True

client = ViberBot(intents=intents)
client.run(TOKEN)
