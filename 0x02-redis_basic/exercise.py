#!/usr/bin/env python3
"""
Main file
"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def replay(fn: Callable) -> None:
    """ Function to display the history of calls
        of a particular function.
    """
    name = fn.__qualname__
    self = fn.__self__
    count = self.get(name, self.get_int())
    print("{} was called {} times:".format(name, count))
    inputs = self._redis.lrange("{}:inputs".format(name), 0, -1)
    outputs = self._redis.lrange("{}:outputs".format(name), 0, -1)

    result = zip(inputs, outputs)
    for k, v in result:
        print('{}(*{}) -> {}'.format(name, self.get_str()(k),
                                     self.get_str()(v)))


def call_history(method: Callable) -> Callable:
    """ Decorator function that stores the history of
        inputs and outputs for a particular function.
    """
    @wraps(method)
    def wrapper(*args, **kwds):
        in_key = "{}:inputs".format(method.__qualname__)
        out_key = "{}:outputs".format(method.__qualname__)
        inputs = str(args[1:])
        outputs = method(*args, **kwds)

        self = args[0]
        self._redis.rpush(in_key, inputs)
        self._redis.rpush(out_key, outputs)
        return outputs
    return wrapper


def count_calls(method: Callable) -> Callable:
    """ Decorator function that counts the number of
        calls of a particular function.
    """
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
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data as a key value pair with uuid
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get_str(self):
        """ Helper function to convert Redis bytes to
            string.
        """
        return bytes.decode

    def get_int(self):
        """ Helper function to convert Redis bytes to
            integer.
        """
        return int

    def get(self, key: str, fn: Callable[[bytes],
            Union[str, bytes, int, float]] = None):
        """ Function that gets a value using a key
            from the store.
        """
        value = self._redis.get(key)
        if value is not None:
            if fn is not None:
                return fn(value)
            return value
