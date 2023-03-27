#!/usr/bin/env python3
"""
Main file
"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(*args, **kwds):
        name = method.__qualname__
        self = args[0]

        self._redis.incr(name)
        return method(*args, **kwds)
    return wrapper


class Cache:
    """Cache class
    """
    def __init__(self):
        """Initializes the Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data as a key value pair with uuid
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get_str(self):
        """
        """
        return str

    def get_int(self):
        """
        """
        return int

    def get(self, key: str, fn: Callable[[bytes],
            Union[str, bytes, int, float]] = None):
        """
        """
        value = self._redis.get(key)
        if value is not None:
            if fn is not None:
                return fn(value)
            return value


# c = Cache()
# c.store('boy')
