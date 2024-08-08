#!/usr/bin/env python3
""" LRU caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class"""

    def __init__(self):
        super().__init__()
        self.lru_keys = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.lru_keys.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            if key in self.lru_keys:
                self.lru_keys.remove(key)
            self.lru_keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            returned_value = self.cache_data[key]
            self.lru_keys.remove(key)
            self.lru_keys.append(key)
            return returned_value
