import asyncio

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from aiogram.webhook.aiohttp_server import (
    SimpleRequestHandler,
    setup_application,
)
from aiohttp.web import run_app
from aiohttp.web_app import Application
from config import conf
from db import db
from handlers.auth import auth_router
from handlers.button_handlers import buttons_router
from handlers.order_taxi import order_taxi_router
from utils.tables import create_tables
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from main import main_router

async def on_startup(dispatcher: Dispatcher, bot: Bot):
    await db.connect()
    await create_tables()
    await bot.set_my_commands([
        BotCommand(command='start', description='botni start qiladi'),
        BotCommand(command='cancel', description='bekor qilish')
    ])
    await bot.set_webhook(f"{conf.bot.BASE_URL}{conf.bot.BOT_PATH}")


def main():
    session = AiohttpSession()
    bot = Bot(conf.bot.TOKEN, session=session, parse_mode="HTML")

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(main_router)
    dp.include_router(buttons_router)
    dp.include_router(auth_router)
    dp.include_router(order_taxi_router)
    dp.startup.register(on_startup)
    dp.shutdown.register(db.close)

    app = Application()

    SimpleRequestHandler(dispatcher=dp, bot=bot).register(
        app, path=conf.bot.BOT_PATH
    )

    setup_application(app, dp, bot=bot)

    run_app(app, host=conf.bot.WEB_SERVER_HOST, port=conf.bot.WEB_SERVER_PORT)


if __name__ == '__main__':
    main()