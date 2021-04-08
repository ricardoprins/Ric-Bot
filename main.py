from get_secrets import SecretsStore
import discord
import json

from modules.event import handler as eventHandler
from modules.meme import handler as memeHandler
from modules.tweet import handler as tweetHandler

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send("pong")

        # revert to when a meme command is made
        # you can use a normal reddit api which you feel comfy with.
        # which ever you use make it sure that you document it very well in
        # your modules.
        elif message.content == '!memes':
            await message.channel.send(memeHandler.get_memes())
        
        # revert to when some one asks for events
        # we will have to talk to the people who are building our website to
        # get more info on how they will be arranging the events.
        # if they take time we can implement something quickly.
        elif message.content == '!events':
            await message.channel.send(eventHandler.get_events())

        # revert to when someone asks for tweets
        # there is also a listener file in the module which you can use to
        # listen to tweet updates and then fire a message well thats 
        # unimplemented and really upto you how you want to go with it.
        elif message.content == '!tweets':
            await message.channel.send(tweetHandler.get_tweets())

client = MyClient()

store = SecretsStore()
all_secrets = store.get_all_secrets()
client.run(all_secrets[store.stored_secrets_keys[0]])