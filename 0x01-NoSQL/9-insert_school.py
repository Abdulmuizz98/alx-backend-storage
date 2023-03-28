#!/usr/bin/env python3
"""Contains the function insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """ Inserts a document in a collection using kwargs
    """
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
