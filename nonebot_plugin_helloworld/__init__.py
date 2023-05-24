from nonebot import on_message
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.matcher import Matcher
from nonebot.typing import T_State

I18N = {
    "hello": "world",
    "你好": "世界",
}


async def hello_rule(event: MessageEvent, state: T_State) -> bool:
    key = event.message.extract_plain_text()
    for k, v in I18N.items():
        if key == k:
            state["reply"] = v
            return True
    return False


helloworld = on_message(rule=hello_rule)


@helloworld.handle()
async def _(matcher: Matcher, state: T_State) -> None:
    reply: str = state["reply"]
    await matcher.send(reply)
