#!/usr/bin/env python3
"""The FIFO caching algrorithm"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """the fifo cache class"""

    def __init__(self):
        """first method on class call"""
        super().__init__()

    def put(self, key, item):
        """inserts the item into the cache"""
        if key and item:
            self.cache_data.update({key: item})
        cache_len = len(self.cache_data.items())
        if cache_len > BaseCaching.MAX_ITEMS:
            key_of_first_in = list(self.cache_data.items())[0][0]
            self.cache_data.pop(key_of_first_in)
            print('DISCARD: {}'.format(key_of_first_in))

    def get(self, key):
        """return the linked key value from self.cache_data"""
        return self.cache_data.get(key)
