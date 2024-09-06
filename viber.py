import os

import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Access the token from the environment variables
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
