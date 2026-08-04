from loguru import logger

from app.config.constants import LOG_DIR
from app.config.settings import settings

LOG_DIR.mkdir(parents=True, exist_ok=True)

logger.remove()

logger.add(
    LOG_DIR / "assistant.log",
    level=settings.log_level,
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    enqueue=True,
    backtrace=True,
    diagnose=settings.debug,
)

logger.add(
    sink=lambda msg: print(msg, end=""),
    level=settings.log_level,
)

app_logger = logger
