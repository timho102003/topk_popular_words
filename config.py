import logging
from pathlib import Path

from nltk.corpus import stopwords

stopwords = set(stopwords.words("english"))

# Terminal Color:
class bcolors:
    HEADER = "\033[95m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


class myLogger:
    def __init__(
        self,
        logfmt="%(asctime)s: %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d:%H:%M:%S",
    ):

        # create logger
        loggerName = Path(__file__).stem
        # create logging formatter
        logFormatter = logging.Formatter(
            fmt=logfmt,
            datefmt=datefmt,
        )
        loglvl = getattr(logging, "DEBUG")
        self.logger = logging.getLogger(loggerName)
        self.logger.setLevel(loglvl)
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(loglvl)
        consoleHandler.setFormatter(logFormatter)
        self.logger.addHandler(consoleHandler)

    def info(self, msg, bold=False):
        self.logger.info(
            f"{bcolors.BOLD if bold else ''}{msg}{bcolors.ENDC if bold else ''}"
        )

    def debug(self, msg, bold=False):
        self.logger.debug(
            f"{bcolors.BOLD if bold else ''}{msg}{bcolors.ENDC if bold else ''}"
        )

    def header(self, msg, bold=True):
        self.logger.info(
            f"{bcolors.BOLD if bold else ''}{bcolors.HEADER}{msg}{bcolors.ENDC if bold else ''}{bcolors.ENDC}"
        )

    def warning(self, msg, bold=True):
        self.logger.warning(
            f"{bcolors.BOLD if bold else ''}{bcolors.WARNING}{msg}{bcolors.ENDC if bold else ''}{bcolors.ENDC}"
        )

    def fail(self, msg, bold=True):
        self.logger.warning(
            f"{bcolors.BOLD if bold else ''}{bcolors.FAIL}{msg}{bcolors.ENDC if bold else ''}{bcolors.ENDC}"
        )


__all__ = ["myLogger", "stopwords", "bcolors"]
