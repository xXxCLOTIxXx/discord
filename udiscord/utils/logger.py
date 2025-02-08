import logging
from datetime import datetime
from colorama import Fore, Style, init


init(autoreset=True)

class Logger:
    """
    A customizable logging class with colorized output.

    Supports different logging levels with color-coded messages 
    for improved readability in the console.
    """

    def __init__(self, level=logging.INFO):
        """
        Initializes the logger with a specified logging level.

        :param level: The minimum logging level to display (default: INFO).
        """
        self.logger = logging.getLogger("Logger")
        self.logger.setLevel(level)
        
        self.console_handler = logging.StreamHandler()

        self.COLORS = {
            logging.DEBUG: Fore.GREEN,
            logging.INFO: Fore.CYAN,
            logging.WARNING: Fore.YELLOW,
            logging.ERROR: Fore.RED,
            logging.CRITICAL: Fore.RED
        }

        self.LEVEL_COLORS = {
            logging.DEBUG: Fore.GREEN + Style.BRIGHT,
            logging.INFO: Fore.CYAN + Style.BRIGHT,
            logging.WARNING: Fore.YELLOW + Style.BRIGHT,
            logging.ERROR: Fore.RED + Style.BRIGHT,
            logging.CRITICAL: Fore.RED + Style.BRIGHT
        }
        self.DATE_COLOR = Fore.LIGHTBLACK_EX

        formatter = logging.Formatter(fmt="%(message)s")

        self.console_handler.setFormatter(formatter)
        self.logger.addHandler(self.console_handler)

    def _colorize(self, message, level):

        level_name = logging.getLevelName(level)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        colored_timestamp = self.DATE_COLOR + timestamp + Style.RESET_ALL
        colored_level = self.LEVEL_COLORS.get(level, Fore.WHITE) + level_name + Style.RESET_ALL
        colored_message = self.COLORS.get(level, Fore.WHITE) + message + Style.RESET_ALL

        return f"{colored_timestamp} - {colored_level} - {colored_message}"

    def info(self, message):
        """
        Logs an informational message.

        :param message: The message to log.
        """
        colored_message = self._colorize(message, logging.INFO)
        self.logger.info(colored_message)

    def warning(self, message):
        """
        Logs a warning message.

        :param message: The message to log.
        """
        colored_message = self._colorize(message, logging.WARNING)
        self.logger.warning(colored_message)

    def error(self, message):
        """
        Logs an error message.

        :param message: The message to log.
        """
        colored_message = self._colorize(message, logging.ERROR)
        self.logger.error(colored_message)

    def debug(self, message):
        """
        Logs a debug message.

        :param message: The message to log.
        """
        colored_message = self._colorize(message, logging.DEBUG)
        self.logger.debug(colored_message)

    def critical(self, message):
        """
        Logs a critical error message.

        :param message: The message to log.
        """
        colored_message = self._colorize(message, logging.CRITICAL)
        self.logger.critical(colored_message)

    def set_level(self, level):
        """
        Sets the logging level.

        :param level: The new logging level (e.g., logging.DEBUG, logging.ERROR).
        """
        self.logger.setLevel(level)
