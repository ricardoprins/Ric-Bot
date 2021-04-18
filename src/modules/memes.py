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

    lenUrl = len(image_urls)

    for i in range(lenUrl):
        modstring = str(image_urls[i]).split("b'")[1]
        modstring = modstring[:-1]
        image_urls[i] = modstring

    return image_urls[random.randint(0, postLimit - 1)]
