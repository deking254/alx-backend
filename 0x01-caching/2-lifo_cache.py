#!/usr/bin/env python3
"""The FIFO caching algrorithm"""
import time
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """the fifo cache class"""
    last_modified = {}
    time_list = []
    key_last = None

    def __init__(self):
        """first method on class call"""
        super().__init__()

    def put(self, key, item):
        """inserts the item into the cache"""
        if key and item:
            self.time_list = []
            if len(self.cache_data.items()) == BaseCaching.MAX_ITEMS:
                sorted_values = self.last_modified.values()
                for value in sorted_values:
                    self.time_list.append(value)
                self.time_list.sort()
                for ki in self.last_modified.items():
                    if ki[1] == self.time_list[-1]:
                        self.key_last = ki[0]
            self.last_modified.update({key: time.time()})
            self.cache_data.update({key: item})
            cache_len = len(self.cache_data.items())
            if cache_len > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.key_last)
                self.last_modified.pop(self.key_last)
                print('DISCARD: {}'.format(self.key_last))

    def get(self, key):
        """return the linked key value from self.cache_data"""
        return self.cache_data.get(key)
