import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from app.core.handlers import handlers_router
from app.settings.config import Config, load_config

logging.basicConfig(
    format=f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    level=logging.DEBUG,
)


def setup_routers(dp: Dispatcher) -> None:
    dp.include_router(handlers_router)


async def main():
    config: Config = load_config()
    bot = Bot(config.bot.token, parse_mode=config.bot.parse_mode)
    dp = Dispatcher(storage=RedisStorage.from_url(config.redis.url))

    setup_routers(dp)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await dp.storage.close()


if __name__ == "__main__":
    asyncio.run(main())
