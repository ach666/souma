import discord
import os
import asyncio

client = discord.Client()

async def my_background_task():
    await client.wait_until_ready()
    channel = discord.Object(id='531423912538537995')
    while not client.is_closed:
        await client.send_message(channel, "sword")
        await asyncio.sleep(10) # task runs every 60 seconds

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
client.loop.create_task(my_background_task())
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
