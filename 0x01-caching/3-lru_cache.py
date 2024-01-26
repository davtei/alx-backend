#!/usr/bin/env python3
""" LRU Caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache System """

    def __init__(self):
        """ Initialize LRU Cache """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.usage.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.usage.pop(0)
            del self.cache_data[discard]
            print(f"DISCARD: {discard}")
        self.usage.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        self.usage.remove(key)
        self.usage.append(key)
        return self.cache_data[key]
