"""
This module controls the Discord client behavior.

Classes: Discord
Functions: runClient()
"""
from discord import Client
from modules.memes import get_memes
from modules.settings import loadSettings, runDiscordBot
from modules.quotes import getQuote
from modules.antispam import has_links
from modules.help import help


class Discord(Client):
    """
    Discord bot client class.

    Methods:
        on_ready(self)
        on_message(self, message)
    """

    async def on_ready(self):
        """Displays success message if connection is successful."""
        print("Logged on as", self.user)

    async def on_message(self, message):
        """
        Controls the bot's behavior upon reading a message on the chat.

        This method of controlling the bot will soon be replaced by one
        that will be more efficient and easier to edit.
        Args:
            message: chat message from Discord
        """
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
            await message.channel.send(
                "Links not allowed in this channel", delete_after=15
            )


def runClient():
    """This method loads the environment variables and runs the Discord bot client."""
    loadSettings()
    client = Discord()
    runDiscordBot(client)
