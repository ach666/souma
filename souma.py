import discord
import os
import time

client = discord.Client()

async def my_background_task():
    await client.wait_until_ready()
    channel = discord.Object(id='531423912538537995')
    while not client.is_closed:
        await client.send_message(channel, "sword")
        await asyncio.sleep(900)
 
client.loop.create_task(my_background_task())
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
