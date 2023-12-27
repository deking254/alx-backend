#!/usr/bin/env python3
"""pagination tasks one"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """return a tuple of size two containing a start index and an end index"""
    first_index = 0
    for _ in range(0, page - 1):
        first_index += page_size
    last_index = first_index + page_size
    return (first_index, last_index)
