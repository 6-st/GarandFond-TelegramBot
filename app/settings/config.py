import os
from dataclasses import dataclass
from app.settings.bot import Bot
from app.settings.database import DB, Redis
from dotenv import load_dotenv
import os


@dataclass
class Config:
    """Configurator"""

    bot: Bot
    db: DB
    redis: Redis


def load_config() -> Config:
    load_dotenv()
    return Config(
        bot=Bot(
            token=os.environ["BOT_TOKEN"],
            parse_mode=os.getenv("BOT_PARSEMODE", "HTML"),
        ),
        db=DB(
            host=os.getenv("DB_HOST", "localhost"),
            name=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
        ),
        redis=Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=os.getenv("REDIS_PORT", "6309"),
            db=os.getenv("REDIS_DB", "0"),
            user=os.getenv("REDIS_USER", ""),
            password=os.getenv("REDIS_PASSWORD", ""),
        ),
    )
