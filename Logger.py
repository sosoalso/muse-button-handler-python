# ---------------------------------------------------------------------------- #
import logging
import os
from logging.handlers import RotatingFileHandler


class Logger:
    """
    A custom logger class that provides logging functionality with different log levels.

    Args:
        name (str): The name of the logger.
        level (int, optional): The log level to set for the logger. Defaults to logging.INFO.

    Attributes:
        INFO (int): Log level for informational messages.
        DEBUG (int): Log level for debugging messages.
        WARNING (int): Log level for warning messages.
        ERROR (int): Log level for error messages.
        CRITICAL (int): Log level for critical messages.

    Methods:
        get_logger: Returns the logger instance.

    Example:
        logger = Logger("my_logger")
        logger.get_logger().info("This is an informational message.")
    """

    INFO = logging.INFO
    DEBUG = logging.DEBUG
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    def __init__(self, name, level=logging.INFO):
        """
        Initializes the Logger instance.

        Args:
            name (str): The name of the logger.
            level (int, optional): The log level to set for the logger. Defaults to logging.INFO.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        fh = RotatingFileHandler(f"{log_dir}/{name}.log", maxBytes=1024 * 1024 * 5, backupCount=5)
        fh.setLevel(level)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def get_logger(self):
        """
        Returns the logger instance.

        Returns:
            logging.Logger: The logger instance.
        """
        return self.logger


# ---------------------------------------------------------------------------- #
