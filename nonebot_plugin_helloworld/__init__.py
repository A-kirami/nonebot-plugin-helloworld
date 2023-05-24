from typing import NoReturn

from nonebot import on_fullmatch
from nonebot.internal.adapter import Event
from nonebot.matcher import Matcher

I18N = {
    "hello": "world",
    "你好": "世界",
}


helloworld = on_fullmatch(tuple(I18N.keys()), ignorecase=True)


@helloworld.handle()
async def _(matcher: Matcher, event: Event) -> NoReturn:
    await matcher.finish(I18N[event.get_plaintext().lower()])
