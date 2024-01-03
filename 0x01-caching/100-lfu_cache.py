#!/usr/bin/env python3
"""The FIFO caching algrorithm"""
import time
from typing import DefaultDict

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """the fifo cache class"""
    last_modified = {}
    time_list = []
    key_last = None
    use_frequency = DefaultDict(int)

    def __init__(self):
        """first method on class call"""
        super().__init__()

    def put(self, key, item):
        """inserts the item into the cache"""
        if key and item:
            self.time_list = []
            if len(self.cache_data.items()) == BaseCaching.MAX_ITEMS:
                sorted_frequencies = list(self.use_frequency.values())
                sorted_frequencies.sort()
                number_lfus = sorted_frequencies.count(sorted_frequencies[0])
                if number_lfus > 1:
                    matching_frequencies = []
                    time_values = []
                    for matches in self.use_frequency.items():
                        if matches[1] == sorted_frequencies[0]:
                            matching_frequencies.append(matches[0])
                    for matching_count_key in matching_frequencies:
                        time_val = self.last_modified.get(matching_count_key)
                        if time_val is not None:
                            time_values.append(time_val)
                    time_values.sort()
                    for ki in self.last_modified.items():
                        if ki[1] == time_values[0]:
                            self.key_last = ki[0]
                elif number_lfus == 1:
                    for keey in self.use_frequency.items():
                        if keey[1] == sorted_frequencies[0]:
                            self.key_last = keey[0]
            self.last_modified.update({key: time.time()})
            self.cache_data.update({key: item})
            self.use_frequency[key] += 1
            cache_len = len(self.cache_data.items())
            if cache_len > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.key_last)
                self.last_modified.pop(self.key_last)
                self.use_frequency.pop(self.key_last)
                print('DISCARD: {}'.format(self.key_last))

    def get(self, key):
        """return the linked key value from self.cache_data"""
        if self.cache_data.get(key) is not None:
            self.last_modified.update({key: time.time()})
            self.use_frequency[key] += 1
        return self.cache_data.get(key)
