#!/usr/bin/env python3
"""List all documents in Python
"""

from pymongo import MongoClient


def list_all(mongo_collection) -> list:
    """List all documents in a collection
    """
   documents = list(mongo_collection.find({}))

    return documents
