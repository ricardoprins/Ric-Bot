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


def runClient():
    loadSettings()
    client = Discord()
    runDiscordBot(client)
