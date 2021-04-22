"""
This module implements the antispam feature for the bot.

Functions: has_links(message)
"""

from re import search

links_not_allowed = (
    829038892145311775,
    829039782260244561,
)  # moderator only and welcome channel
allowed_url = "https://github.com/"


def has_links(message) -> bool:
    """
    Checks if message that contains links was posted in an allowed channel.

    Args: message from Discord chat

    Returns: True or False, depending on channel check.
    """
    url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'#\".,<>?«»“”‘’]))"
    if (
        search(url_regex, message.content)
        and message.channel.id in links_not_allowed
        and allowed_url not in message.content
    ):
        return True
    return False
