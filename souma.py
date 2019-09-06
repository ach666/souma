import discord
import os
import asyncio
import random

client = discord.Client()

sayings = ["do not lament over the rotten souls of those you hath slain in thy battlefield", "you mean a lot  to me", "i will be  your samurai in times of darkness.", "adonith-dono hhot.", "you are always doing your best. I am proud of you", "you will reach your dreams with your own power, but i will be willing to help you along the way if you need.", "i shall give you my blessings for a long, fruitfull and fulfilling life.", "you have so much potential. don't give up no matter what","I shall be with you with every step you take because i have put my full belief in you", "you rocku"]

async def my_background_task():
    await client.wait_until_ready()
    channel = discord.Object(id='619203985022386207')
    while not client.is_closed:
        await client.send_message(channel, "take your meds")
        await client.send_message(channel, random.choice(sayings))
        await asyncio.sleep(15000)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
client.loop.create_task(my_background_task())
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
