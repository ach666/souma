import discord
import os
import asyncio
import random

client = discord.Client()

sayings = ["do not lament over the rotten souls of those you hath slain in thy battlefield", "you mean a lot  to me", "i will be  your samurai in times of darkness.", "adonith-dono hhot."]

async def my_background_task():
    await client.wait_until_ready()
    channel = discord.Object(id='542037405356523528')
    while not client.is_closed:
        await client.send_message(channel, "buy your meds")
        await client.send_message(channel, random.choice(sayings))
        await asyncio.sleep(5000)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
client.loop.create_task(my_background_task())
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
