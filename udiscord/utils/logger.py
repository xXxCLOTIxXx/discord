import logging
from datetime import datetime

class Logger:
    def __init__(self, level=logging.INFO):
        self.logger = logging.getLogger("Logger")
        self.logger.setLevel(level)
        
        self.console_handler = logging.StreamHandler()


        formatter = logging.Formatter(
            fmt="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        self.console_handler.setFormatter(formatter)

        self.logger.addHandler(self.console_handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

    def critical(self, message):
        self.logger.critical(message)

    def set_level(self, level):
        self.logger.setLevel(level)
        
    def add_custom_message(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        custom_message = f"{timestamp} - CUSTOM - {message}"
        self.logger.info(custom_message)