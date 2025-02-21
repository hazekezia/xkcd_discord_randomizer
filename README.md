# XKCD Discord Bot

Automated bot for posting random XKCD comics to a Discord channel.

## Features
- Fetches a random XKCD comic from the official XKCD API.
- Posts the comic as an embedded message in a specified Discord channel.
- Runs automatically on startup.

## Requirements
- Python 3.8+
- `discord.py` for interacting with Discord.
- `aiohttp` for making asynchronous HTTP requests.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/hazekezia/xkcd_discord_randomizer.git
   cd xkcd_discord_randomizer
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up your Discord bot:
   - Create a bot on the [Discord Developer Portal](https://discord.com/developers/applications).
   - Enable `MESSAGE CONTENT INTENT` in bot settings.
   - Copy the bot token.

4. Configure the bot:
   - Edit `TOKEN` in `bot.py` and replace it with your actual bot token.
   - Set `CHANNEL_NAME` to the name of the channel where comics should be posted.

5. Run the bot:
   ```sh
   python main.py
   ```

## Automating with Cron Job

If everything is working correctly, you can automate the comic posting using a cron job. For example, to send an XKCD comic every day at 5 PM, add the following line to your crontab:

```sh
0 17 * * * /usr/bin/python3 <your_code_directory>
```

To edit your crontab, run:

```sh
crontab -e
```
## Example Output
The bot will post messages like this in the specified Discord channel:

**Title: "Light Hacks"**  
[https://xkcd.com/1234](https://xkcd.com/2024)

![XKCD Comic](https://imgs.xkcd.com/comics/light_hacks.png)

## Notes
- The bot must have `Send Messages` and `Embed Links` permissions in the target channel.
- Ensure the bot is in the correct Discord server.

## License
This project is licensed under the MIT License.

