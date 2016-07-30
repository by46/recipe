import logging
import logging.config
import logging.handlers
import os
import os.path
import sys

import colorama

from recipe.utils.path import ensure_dir

WINDOWS = (sys.platform.startswith("win") or
           (sys.platform == 'cli' and os.name == 'nt'))


def config_logging(options):
    if options.verbose == 2:
        level = 'INFO'
    elif options.verbose >= 3:
        level = 'DEBUG'
    else:
        level = 'WARNING'

    if not options.log:
        options.log = os.path.join(os.path.expanduser('~'), 'recipe.log')

    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'exclude_warnings': {
                '()': 'recipe.utils.log.MaxLevelFilter',
                'level': logging.WARNING
            }
        },
        'formatters': {
            'line': {
                'format': '%(message)s'
            }
        },
        'handlers': {
            'console': {
                'level': level,
                'class': 'recipe.utils.log.ColorizedStreamHandler',
                'stream': 'ext://sys.stdout',
                'filters': ['exclude_warnings'],
                'formatter': 'line'
            },
            'console_errors': {
                'level': 'WARNING',
                'class': 'recipe.utils.log.ColorizedStreamHandler',
                'stream': 'ext://sys.stderr',
                'formatter': 'line'
            },
            "user_log": {
                "level": "DEBUG",
                "class": "pip.utils.logging.BetterRotatingFileHandler",
                "filename": options.log,
                "delay": True,
                "formatter": "line",
            },
        },
        'loggers': {
            'recipe': {
                'level': 'WARNING' if level in ['INFO', 'ERROR'] else 'DEBUG',
                'handlers': ['console', 'console_errors', 'user_log'],
                'propagate': False
            }
        }
    })


def _color_wrap(*colors):
    def wrapped(inp):
        return "".join(list(colors) + [inp, colorama.Style.RESET_ALL])

    return wrapped


class ColorizedStreamHandler(logging.StreamHandler):
    COLORS = [
        (logging.ERROR, _color_wrap(colorama.Fore.RED)),
        (logging.WARNING, _color_wrap(colorama.Fore.YELLOW))
    ]

    def __init__(self, stream=None):
        super(ColorizedStreamHandler, self).__init__(stream)

        if WINDOWS:
            self.stream = colorama.AnsiToWin32(self.stream)

    def should_color(self):
        real_stream = (
            self.stream if not isinstance(self.stream, colorama.AnsiToWin32)
            else self.stream.wrapped
        )

        if hasattr(real_stream, 'isatty') and real_stream.isatty():
            return True

        if os.environ.get("TERM") == "ANSI":
            return True

        return False

    def format(self, record):
        msg = super(ColorizedStreamHandler, self).format(record)
        if self.should_color():
            for level, color in self.COLORS:
                if record.levelno >= level:
                    msg = color(msg)
                    break

        return msg


class BetterRotatingFileHandler(logging.handlers.RotatingFileHandler):
    def _open(self):
        ensure_dir(os.path.dirname(self.baseFilename))
        return super(BetterRotatingFileHandler, self)._open()


class MaxLevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno < self.level
