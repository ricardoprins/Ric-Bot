"""
This module implements the help command for the bot.

Functions: help()
"""


def help() -> str:
    """
    Returns the command list as a string.
    """

    return """
commands
    !help:\t Help menu
    ping:\t Replies with pong
    !memes:\t Fetchs a random meme from reddit
    !quotes:\t Displays a quote
"""
