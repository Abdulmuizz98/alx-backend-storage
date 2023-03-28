#!usr/bin/env python3
"""Contains get_page function
"""
import requests
from typing import Callable
from functools import wraps
import redis


cache = redis.Redis()


def count_url_visits(method: Callable):
    """ Decorator function that keeps count of 
        the number of times a url is visited and 
        caches the result of the visit for 10 seconds.
    """
    @wraps(method)
    def wrapper(*args, **kwds):
        url = args[0]
        key = 'count:{}'.format(url)
        cache.incr(key)
        result = method(*args, **kwds)
        cache.set(url, result)
        cache.expire(url, 10)
        return result
    return wrapper


@count_url_visits
def get_page(url: str) -> str:
    """ Requests a url and return result
    """
    r = requests.get(url)
    return r.text
