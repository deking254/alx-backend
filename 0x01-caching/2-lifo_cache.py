#!/usr/bin/env python3
"""The FIFO caching algrorithm"""
import time
BaseCaching = __import__('base_caching').BaseCaching

class LIFOCache(BaseCaching):
    """the fifo cache class"""
    last_modified = {}
    time_list=[]
    key_last = None
    def __init__(self):
        """first method on class call"""
        super().__init__()

    def put(self, key, item):
        """inserts the item into the cache"""
        if key and item:

            self.cache_data.update({key: item})
            self.last_modified.update({key: time.time()})
            sorted_values = self.last_modified.values()
            for value in sorted_values:
                self.time_list.append(value)
            self.time_list.sort()
            for key in self.time_list:
                print(key)
            cache_len = len(self.cache_data.items())
            if cache_len > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.last_modified)
                self.existing_key = False
                print('DISCARD: {}'.format(self.last_modified))

    def get(self, key):
        """return the linked key value from self.cache_data"""
        return self.cache_data.get(key)
