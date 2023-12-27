#!/usr/bin/env python3
"""pagination tasks one"""


def index_range(page, page_size):
    """return a tuple of size two containing a start index and an end index"""
    first_index = 0
    for _ in range(0, page - 1):
        first_index += page_size
    last_index = first_index + page_size
    return (first_index, last_index)

