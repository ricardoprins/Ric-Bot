from discord import Client
from modules.memes import get_memes
from modules.settings import loadSettings, runDiscordBot
from modules.quotes import getQuote


class Discord(Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):  # refactor this to commands module later on
        if message.author == self.user:
            return

        if message.content == "ping":
            await message.channel.send("pong")

        elif message.content == "!memes":
            await message.channel.send(await get_memes())

        elif message.content == "!quotes":
            await message.channel.send(getQuote())

        elif message.content == "!events":
            await message.channel.send(events.get_events())
        
        if antispam.has_links(message):
            await message.delete()
            await message.channel.send("Links not allowed in this channel", delete_after=15)


def runClient():
    loadSettings()
    client = Discord()
    runDiscordBot(client)