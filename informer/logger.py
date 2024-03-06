import logging
from datetime import datetime
from functools import wraps

from config import LOG_DIR


filename = LOG_DIR / "{:%Y-%m-%d}.log".format(datetime.now())

formatter = logging.Formatter(
    fmt="%(levelname)s, %(asctime)s: %(message)s",
    datefmt="%H:%M:%S",
)

handler = logging.FileHandler(filename)
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
logger.addHandler(handler)


def log_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            args_repr = [str(a) for a in args]
            kwargs_repr = [f"{k!s}={v!s}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr) or None
            logger.error(
                f"{func.__name__}({signature}): {error!s}"
            )
    return wrapper
