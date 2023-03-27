#!/usr/bin/env python3
"""
Main file
"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(fn: Callable):
    @wraps(fn)
    def wrapper(*args, **kwds):
        name = fn.__qualname__
        rd = args[0]._redis

        rd.incr(name)
        return fn(*args, **kwds)
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


c = Cache()
c.store('boy')
