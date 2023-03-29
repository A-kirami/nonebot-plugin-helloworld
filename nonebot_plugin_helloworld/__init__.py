from nonebot import on_message
from nonebot.matcher import Matcher
from nonebot.params import EventPlainText
from nonebot.internal.adapter import Event


async def rule_check_head(text: str = EventPlainText()) -> bool:
    return text in I18N



helloworld = on_message(rule=rule_check_head, priority=5, block=False)


@helloworld.handle()
async def _(matcher: Matcher, event: Event) -> None:
    key = event.get_plaintext()
    await matcher.send(I18N[key])


I18N = {
    "hello": "world",
    "你好": "世界"
}
