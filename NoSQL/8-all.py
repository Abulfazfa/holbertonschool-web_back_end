#!/usr/bin/env python3
"""List all documents in Python
"""

import pymongo


def list_all(mongo_collection) -> list:
    """List all documents in a collection
    """
    documents = mongo_collection.find()
    if documents.count() == 0:
        return []

    return list(documents)
