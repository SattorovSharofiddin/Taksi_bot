import re
from aiogram.filters import Filter
from aiogram.types import Message


class NotRegex(Filter):
    def __init__(self, pattern: str) -> None:
        self.pattern = pattern

    async def __call__(self, message: Message) -> bool:
        return not re.match(self.pattern, message.text)