#!/usr/bin/env python3
"""caching algorithms"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """the basic cache class"""

    def put(self, key, item):
        """insert data into the self.cache_data dict"""
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """returns data from self.cache_data"""
        return self.cache_data.get(key)
