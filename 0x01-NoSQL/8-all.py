#!/usr/bin/env python3
"""Contains the function list_all
"""


def list_all(mongo_collection):
    """ Lists all documents in a collection
    """
    docs = mongo_collection.find({})
    if not list(docs):
        return []
    return docs
