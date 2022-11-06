import discord

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

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTAyNzIyNzk1MDM4ODYyMTM2Mw.GoE8jw.-9iFcXJJZPoxFjkjnU49cOrX8F2CDcg7SrnqgE')
