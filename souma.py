import discord
import os
import time

client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(game=discord.Game(name="hanafuda"))

async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id='channel_id_here')
    while not client.is_closed:
        counter += 1
        await client.send_message(channel, counter)
        await asyncio.sleep(1800)
 
client.loop.create_task(my_background_task())
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
