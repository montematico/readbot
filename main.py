import discord
import datetime
import json

# read file

with open('config.json', 'r') as myfile:
    data=myfile.read()
# parse file
config = json.loads(data)

#setup n' shit
client = discord.Client()

@client.event
async def on_ready():
    print('Darryl is online {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="With your heart"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!read' or '!r' or '!seen'):
        today = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        await message.channel.send("read by: " + str(message.author) + " at: " + str(today))
        await message.delete()

client.run(config["token"])

