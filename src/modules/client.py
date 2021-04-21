from discord import Client
from modules.memes import get_memes
from modules.settings import loadSettings, runDiscordBot
from modules.quotes import getQuote
from modules.antispam import has_links
from modules.help import help


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

        elif message.content == "!help":
            await message.channel.send(help())

        if has_links(message):
            await message.delete()
            await message.channel.send("Links not allowed in this channel", delete_after=15)


def runClient():
    loadSettings()
    client = Discord()
    runDiscordBot(client)
