"""
a util for logging
"""

from enum import Enum, auto


class VerbosityLevel(Enum):
    """
    A class for the level of verbosity to be used on the Logger.
    """

    NONE = auto()
    INFO = auto()
    WARNING = auto()
    DEBUG = auto()


class Logger:
    """
    The class for the logger.
    """

    def __init__(self, name, verbosity, file_name=None):
        self.file_name = file_name
        self.name = name
        self.verbosity = verbosity

    def log(self, message: str, verbosity_level: VerbosityLevel):
        """
        Log if verbosity_level is equal or less than verbosity
        """
        if verbosity_level.value <= self.verbosity:
            print(f"[{self.name}:{verbosity_level.name}] {message}")
            if self.file_name is not None:
                with open(self.file_name, "a", encoding="utf-8") as f:
                    f.write(f"[{self.name}:{verbosity_level.name}] {message}\n")
    def info(self, message):
        """
        A wrapper of log()
        """
        self.log(message, VerbosityLevel.INFO)
    def debug(self, message):
        """
        A wrapper of log()
        """
        self.log(message, VerbosityLevel.DEBUG)
