#!/usr/bin/env python3
"""Simple helper function to paginate a dataset"""

import csv
from typing import List
import math
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Calculate the start and end index for a given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
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
        """ function to get page of the dataset """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        dataset: List = self.dataset()
        page_start, page_end = index_range(page, page_size)
        if page_start >= len(dataset) or page_end >= len(dataset):
            return []

        return dataset[page_start:page_end]
