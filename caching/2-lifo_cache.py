#!/usr/bin/env python3
""" LIFO caching """

from base_caching import BaseCaching


class LIFOCache (BaseCaching):
    """ LIFOCache class"""

    def __init__(self):
        """ Initiliaze """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_item = next(reversed(self.cache_data))
                print("DISCARD: {}".format(last_item))
                self.cache_data.pop(last_item)

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            return self.cache_data[key]

