#!/usr/bin/env python3
""" LIFO caching """

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache class"""

    def __init__(self):
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Get the last added item (LIFO)
            last_key = next(reversed(self.cache_data))
            print(f"DISCARD: {last_key}")
            self.cache_data.pop(last_key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
