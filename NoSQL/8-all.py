#!/usr/bin/env python3
"""List all documents in Python
"""

import pymongo


def list_all(mongo_collection) -> list:
    """List all documents in a collection
    """
    mongo_collection = mongo_collection.find()
    if mongo_collection.count() == 0:
        return []

    return list(mongo_collection)
