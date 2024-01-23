#!/usr/bin/python3
""" BasicCache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache defines a caching system in key-value pairs
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """

    def __init__(self):
        """ Initialize class instance """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Store a key-value pair to the cache_data dictionary
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Return value linked to key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
