from loguru import logger

logger.add("bot.log", rotation="10 MB", backtrace=True, diagnose=True)
