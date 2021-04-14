import os
import discord
from os.path import join
from dotenv import load_dotenv
from praw import Reddit


class Settings:

    _BOT_NAME = "Ric-Bot - Discord bot by Tesseract Coding"
    _SUBREDDITS = "funnyterriblefacebookmemes+wholesomememes+ProgrammerHumor+MemeEconomy+memes+AdviceAnimals+sfwmemes+BikiniBottomTwitter"
    _POST_LIMIT = 21  # WARNING - AVOID CHANGING THIS!!!
    SECRETS = {"DISCORD_TOKEN": "", "REDDIT_CLIENT_ID": "", "REDDIT_CLIENT_SECRET": ""}

    def _getSecrets(self):
        try:
            for i in self.SECRETS:
                self.SECRETS[i] = os.environ[i]
        except:
            return "Error in loading environment variables."  # take this check to the loadSettings() function.


def loadReddit():
    reddit = Reddit(
        client_id=Settings.SECRETS["REDDIT_CLIENT_ID"],
        client_secret=Settings.SECRETS["REDDIT_CLIENT_SECRET"],
        user_agent=Settings._BOT_NAME,
    )
    return reddit


def loadSettings():  # to be changed - add a try/catch for the .env file
    dotenv_path = join(os.getcwd(), ".env")
    load_dotenv(dotenv_path)
    settings = Settings()
    Settings._getSecrets(settings)


def getSubreddits():
    return Settings._SUBREDDITS


def getPostLimit():
    return Settings._POST_LIMIT


def runDiscordBot(DiscordClient: discord.Client):
    discord = DiscordClient
    discord.run(Settings.SECRETS["DISCORD_TOKEN"])
