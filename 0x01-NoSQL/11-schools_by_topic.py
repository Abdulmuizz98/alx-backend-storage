#!/usr/bin/env python3
"""Contains the function schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """ return list of schools having a specific topic
    """
    docs = mongo_collection.find({"topics": {"$all": [topic]}})
    return docs
