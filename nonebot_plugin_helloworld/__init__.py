from typing import NoReturn

from nonebot import on_message
from nonebot.internal.adapter import Event
from nonebot.matcher import Matcher
from nonebot.typing import T_State

I18N = {
    "hello": "world",
    "你好": "世界",
}


async def hello_rule(event: Event, state: T_State) -> bool:
    try:
        key = event.get_plaintext().lower()
    except (ValueError, NotImplementedError):
        return False

    if key in I18N:
        state["reply"] = I18N[key]
        return True

    return False


helloworld = on_message(rule=hello_rule)


@helloworld.handle()
async def _(matcher: Matcher, state: T_State) -> NoReturn:
    reply: str = state["reply"]
    await matcher.finish(reply)
