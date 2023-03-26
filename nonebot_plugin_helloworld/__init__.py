from nonebot import on_message
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import MessageEvent


helloworld = on_message()


@helloworld.handle()
async def _(matcher: Matcher, event: MessageEvent) -> None:
    key = event.message.extract_plain_text()
    if key in I18N:
        await matcher.send(I18N[key])


I18N = {
    "hello": "world",
    "你好": "世界"
}
