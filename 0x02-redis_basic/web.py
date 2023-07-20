#!/usr/bin/env python3
""" Module for Implementing an expiring web cache and tracker """

from functools import wraps
import redis
import requests
from typing import Callable

client = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ Decortator to count how many request has been made"""

    @wraps(method)
    def wrapper(url):
        """ Function wrapper """
        client.incr(f"count:{url}")
        cached_html = client.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        client.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Gets the html content of a web page
    """
    req = requests.get(url)
    return req.text
