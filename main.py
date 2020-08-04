import discord
from datetime import time

@client.event
async def on_ready():
    print('Darryl is online {0.user}'.format(client))
    print('loaded in: ' + str(round((time.time() - loadtime),2)) + 's')
    await bot.change_presence(activity=discord.Game(name="With your heart"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('#read'):
        today = date.today()
        await message.channel.send("read by: " + message.author + " at: " + today)

client.run(config["token"])

