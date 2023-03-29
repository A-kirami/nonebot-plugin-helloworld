from nonebot import on_message
from nonebot.matcher import Matcher
from nonebot.params import EventPlainText
from nonebot.adapters.onebot.v11 import MessageEvent


async def rule_check_head(text: str = EventPlainText()) -> bool:
    return text in I18N



helloworld = on_message(rule=rule_check_head, priority=5, block=False)


@helloworld.handle()
async def _(matcher: Matcher, event: MessageEvent) -> None:
    key = event.message.extract_plain_text()
    await matcher.send(I18N[key])


I18N = {
    "hello": "world",
    "你好": "世界"
}
