import discord
import aiohttp
import asyncio
import random

TOKEN = ''  # Your token
CHANNEL_NAME = 'xkcd'  # Your channel name

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    async def on_ready(self):
        print(f'Logged on as {self.user}')
        await self.send_xkcd()
        await self.close()

    async def send_xkcd(self):
        channel = discord.utils.get(self.get_all_channels(), name=CHANNEL_NAME)
        if not channel:
            print(f'Channel "{CHANNEL_NAME}" not found')
            return

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get("https://xkcd.com/info.0.json") as getURL:
                    if getURL.status == 200:
                        json_getURL = await getURL.json()
                        number = random.randint(1, json_getURL['num'])
                        comic_url = f"https://xkcd.com/{number}/info.0.json"
                    else:
                        print('Failed to fetch latest xkcd comic.')
                        return
                
                async with session.get(comic_url) as response:
                    if response.status == 200:
                        json_response = await response.json()
                        img_url = json_response['img']
                        img_title = json_response['title']
                        img_link = f"https://xkcd.com/{json_response['num']}"

                        embed = discord.Embed(title=img_title, url=img_link, description=img_link)
                        embed.set_image(url=img_url)
                        
                        await channel.send(embed=embed)
                    else:
                        print(f'Failed to fetch xkcd comic #{number}.')
            except Exception as e:
                print(f'Error occurred: {e}')

client = MyClient(intents=intents)
client.run(TOKEN)
