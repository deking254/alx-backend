#!/usr/bin/env python3
"""pagination tasks"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns data on a page specified"""
        data = self.dataset()
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0
        list_items = []
        first_last = index_range(page, page_size)
        try:
            for index in range(first_last[0], first_last[1]):
                list_items.append(data[index])
            return list_items
        except Exception:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns metadata about a given page"""
        data = self.dataset()
        total_page = None
        next_page = None
        previous_page = None
        if len(data) % page_size > 0:
            total_page = int(len(data) / page_size) + 1
        else:
            total_page = int(len(data) / page_size)
        if page + 1 <= int(len(data) / page_size):
            next_page = page + 1
        if page - 1 > 0:
            previous_page = page - 1
        hyper = {'page_size': page_size, 'page': page,
                 'data': self.get_page(page, page_size),
                 'next_page': next_page, 'prev_page': previous_page,
                 'total_pages': total_page}
        return hyper


def index_range(page: int, page_size: int) -> Tuple:
    """return a tuple of size two containing a start index and an end index"""
    first_index = 0
    for _ in range(0, page - 1):
        first_index += page_size
    last_index = first_index + page_size
    return (first_index, last_index)
