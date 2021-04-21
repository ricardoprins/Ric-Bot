import random
from .settings import loadReddit, getPostLimit, getSubreddits


async def get_memes():

    reddit = loadReddit()
    postLimit = getPostLimit()
    subreddit = await reddit.subreddit(getSubreddits())
    posts = subreddit.hot(limit=postLimit)
    image_urls, image_titles = [], []

    async for post in posts:
        image_urls.append(post.url.encode("utf-8"))
        image_titles.append(post.title.encode("utf-8"))

    image_urls = [i.decode() for i in image_urls]

    return image_urls[random.randint(0, postLimit - 1)]
