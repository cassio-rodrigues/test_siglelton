

from typing import Any


class MetaSingletonTeste(type):
    """Mesma coisa que com a clase base, porém usando metaclasse"""

    __instances = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaSingletonTeste, cls).__call__(*args, **kwargs)
        return super().__call__(*args, **kwargs)


class Logger(metaclass=MetaSingletonTeste):
    pass


log1 = Logger()
print(f"Log 1: {id(log1)}")


log2 = Logger()
print(f"Log 2: {id(log2)}")