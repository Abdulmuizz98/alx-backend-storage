#!/usr/bin/env python3
"""
Main file
"""
import redis
from uuid import uuid4
from typing import Union, Callable


class Cache:
    """Cache class
    """
    def __init__(self):
        """Initializes the Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

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

    def get(self, key: str, fn: Callable[[bytes], Union[str, bytes, int, float]]=None):
        """
        """
        value = self._redis.get(key)
        if value is not None:
            if fn is not None:
                return fn(value)
            return value

