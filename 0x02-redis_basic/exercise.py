#!/usr/bin/env python3
"""
Main file
"""
import redis
from uuid import uuid4


class Cache:
    """
    """
    def __init__(self):
        """
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: [str | bytes | int | float]) -> str:
        """
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
