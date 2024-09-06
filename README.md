# Viber Discord Bot

Viber is a Discord bot that creates a YouTube playlist based on the user's mood and plays it in a Discord channel.

## Features

- Generate YouTube playlists based on user mood.
- Play the generated playlist in a Discord voice channel.
- Integrates with OpenAI for mood analysis.
- Uses `youtube-dl` for downloading and playing YouTube videos.

## Requirements

- Python 3.12 or higher
- `discord-py` >= 2.4.0
- `openai` >= 1.43.0
- `python-dotenv` >= 1.0.1
- `youtube-dl` >= 2021.12.17

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/viber.git
    cd viber
    ```

2. Install the dependencies:
    ```sh
    pip install .
    ```

3. Create a `.env` file in the root directory and add your OpenAI API key and Discord bot token:
    ```env
    OPENAI_API_KEY="your_openai_api_key"
    DISCORD_BOT_TOKEN="your_discord_bot_token"
    ```

## Usage

1. Run the bot:
    ```sh
    python viber.py
    ```

2. Invite the bot to your Discord server using the OAuth2 URL with the necessary permissions.

3. Use the bot commands in your Discord server to generate and play YouTube playlists based on your mood.

## Commands

- `!mood <your_mood>`: Generates a YouTube playlist based on the specified mood and plays it in the voice channel.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.