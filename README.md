# Viber Discord Bot

![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Viber is a Discord bot that creates a YouTube playlist based on the user's mood and plays it in a Discord channel.

## Table of Contents
- [Viber Discord Bot](#viber-discord-bot)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Commands](#commands)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- Generate YouTube playlists based on user mood.
- Play the generated playlist in a Discord voice channel.
- Integrates with OpenAI for mood analysis.
- Uses `yt-dlp` for downloading and playing YouTube videos.

## Requirements

- ![discord-py](https://img.shields.io/badge/discord--py-%3E%3D2.4.0%2C%20%3C2.5.0-purple)
- ![openai](https://img.shields.io/badge/openai-%3E%3D1.43.0%2C%20%3C2.0.0-green)
- ![python-dotenv](https://img.shields.io/badge/python--dotenv-%3E%3D1.0.1%2C%20%3C2.0.0-yellow)
- ![yt-dlp](https://img.shields.io/badge/yt--dlp-%3E%3D2024.8.6%2C%20%3C2025.0.0-orange)

## Getting Started

To get started with the Viber Discord Bot:

1. Clone this repository and navigate into the directory.
2. Install the dependencies with `pip`.
3. Create a `.env` file and add your OpenAI API key and Discord bot token.
4. Run the bot and invite it to your server.

See the [Installation](#installation) and [Usage](#usage) sections below for detailed instructions.

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

3. Create a `.env` file in the root directory:

    ```sh
    touch .env
    ```

    Then, add your OpenAI API key and Discord bot token:

    ```env
    OPENAI_API_KEY="your_openai_api_key"
    DISCORD_BOT_TOKEN="your_discord_bot_token"
    ```

## Usage

1. Run the bot:
    ```sh
    python viber.py
    ```

2. [Invite the bot to your Discord server](https://discord.com/developers/applications) using the OAuth2 URL with the necessary permissions:

   - Go to your [Discord Developer Portal](https://discord.com/developers/applications).
   - Select your application and navigate to the `Bot` tab.
   - If you haven't already, click `Add Bot`.
   - Ensure that the `Message Content Intent` is enabled.
   - Navigate to the `OAuth2` tab.
   - Ensure that the following scopes and permissions are checked:
     - SCOPES
       - `bot`
     - BOT PERMISSIONS
       - `View Channels`
       - `Send Messages`
       - `Connect`
   - Copy the generated URL and paste it into your browser to invite the bot.

3. Use the bot commands in your Discord server to generate and play YouTube playlists based on your mood.

## Commands

- `!mood <your_mood>`: Generates a YouTube playlist based on the specified mood and plays it in the voice channel.
  - Example: `!mood happy`
  - Supported moods: happy, sad, energetic, relaxed, etc.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
