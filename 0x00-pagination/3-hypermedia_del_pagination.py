#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """returns a dictionary with information such as data and page_size"""
        next_index = None
        items = []
        data = self.indexed_dataset()
        assert int(len(data)) >= index
        first_index = index
        next_index = index + page_size
        valid_indexes = []

        def get_valid_indexes(first_index, next_index):
            """populates a list of valid indexes"""
            for item_index in range(first_index, next_index):
                if len(valid_indexes) < page_size:
                    try:
                        data[item_index]
                        valid_indexes.append(item_index)
                    except Exception:
                        first_index += 1
                        next_index += 1
                        get_valid_indexes(first_index, next_index)
            for i in valid_indexes:
                items.append(data[i])
            return next_index
        next_index = get_valid_indexes(first_index, next_index)
        info = {'index': index, 'data': items,
                'page_size': page_size, 'next_index': next_index}
        return info
