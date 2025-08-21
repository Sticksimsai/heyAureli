from loguru import logger
import os

def setup_logging():
    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level="INFO")
    os.makedirs("logs", exist_ok=True)
    logger.add("logs/aureli.log", rotation="1 MB", retention=3, level="INFO")
    return logger
