#!/usr/bin/env python3
"""
Main file
"""
import redis
from uuid import uuid4
from typing import Union


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
