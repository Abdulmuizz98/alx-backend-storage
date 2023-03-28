#!/usr/bin/env python3
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
        return method(*args, **kwds)
    return wrapper


@count_url_visits
def get_page(url: str) -> str:
    """ Requests a url and return result
    """
    cache_res = cache.get(url)
    if cache.get(url):
        return cache_res

    r = requests.get(url)
    content = r.content
    cache.set(url, content)
    cache.expire(url, 10)
    return content
