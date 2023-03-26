from nonebot import on_fullmatch
from nonebot.matcher import Matcher

helloworld = on_fullmatch("hello")


@helloworld.handle()
async def _(matcher: Matcher) -> None:
    await matcher.send("world")
