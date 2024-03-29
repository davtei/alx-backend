#!/usr/bin/env python3
""" LIFO caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache system """

    def __init__(self):
        """ Initialize class instance """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Store key/value pair to cache_data """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print(f"DISCARD: {self.order[-1]}")
                del self.cache_data[self.order[-1]]
                del self.order[-1]
            if key in self.order:
                del self.order[self.order.index(key)]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Return value linked to key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
