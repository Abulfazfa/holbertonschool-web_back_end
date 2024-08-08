#!/usr/bin/env python3
""" MRU caching """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class """

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last = self.cache_data.popitem()
                print("DISCARD:", last[0])
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            returned_value = self.cache_data[key]
            self.cache_data.pop(key)
            self.cache_data[key] = returned_value
            return returned_value
