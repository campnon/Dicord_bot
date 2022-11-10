import discord
from discord_bot import Bot, stock

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$temp'):
        await message.channel.send('Working on it ...')

    if message.content.startswith('$stock'):
        
        price = stock().temp_data(message)
        await message.channel.send(price)
client.run(Bot().auth())

