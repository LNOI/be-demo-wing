import os
import logging
from pathlib import Path
from fastapi import Request
from logging.handlers import TimedRotatingFileHandler

class CustomLogger():
    def __init__(self,level:str) -> None:
        self.logger = logging.getLogger(level)
        self.logger.setLevel(level=level)
        config_file_logging = {
            "INFO" : "logs/info.log",
            "WARNING" : "logs/warning.log",
            "ERROR" : "logs/error.log",
            "CRITICAL" : "logs/critical.log",
        }
        Path("logs").mkdir(parents=True, exist_ok=True)
        log_handler = TimedRotatingFileHandler(config_file_logging[level], when="D", interval=1, backupCount=7)
        log_formatter = logging.Formatter(
            "%(asctime)s -%(name)s - %(message)s"
        )
        log_handler.setFormatter(log_formatter)
        self.logger.addHandler(log_handler)

    def log(self, message: str):
        self.logger.log(self.logger.level, message)


