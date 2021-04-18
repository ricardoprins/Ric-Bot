from discord import Client
from modules import events
from modules import memes
from modules import settings


class Discord(Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):  # refactor this to commands module later on
        if message.author == self.user:
            return

        if message.content == "ping":
            await message.channel.send("pong")

        elif message.content == "!memes":
            await message.channel.send(memes.get_memes())

        elif message.content == "!events":
            await message.channel.send(events.get_events())
        
        if antispam.has_links(message):
            await message.delete()
            await message.channel.send("Links not allowed in this channel", delete_after=15)


def runClient():
    settings.loadSettings()
    client = Discord()
    settings.runDiscordBot(client)
