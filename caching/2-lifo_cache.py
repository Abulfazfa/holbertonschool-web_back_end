#!/usr/bin/env python3
""" FIFO caching """

from base_caching import BaseCaching


class FIFOCache (BaseCaching):
    """ FIFOCache class"""

    def __init__(self):
        """ Initiliaze """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_item = list(self.cache_data.keys())[-1]
                print("DISCARD: {}".format(last_item))
                self.cache_data.pop(last_item)

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            return self.cache_data[key]
            
