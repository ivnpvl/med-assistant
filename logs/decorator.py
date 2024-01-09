import logging
from functools import wraps

from settings import LOG_FILE


logging.basicConfig(
    level=logging.WARNING,
    filename=LOG_FILE,
    format="%(levelname)s, %(asctime)s: %(message)s",
)


def log_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr) or None
            logging.error(
                f"Исключение в {func.__name__}({signature}): {str(error)}"
            )
    return wrapper
