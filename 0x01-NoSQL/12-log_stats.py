#!/usr/bin/env python3
""" Python script that provides some stats about Nginx logs stored in MongoDB:
"""

from pymongo import MongoClient

client = MongoClient()
nginx_coll = client.logs.nginx
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def count_items(coll, **kwargs):
    """ Count the number of documents with matching
        kwargs in a collection
    """
    return len(list(coll.find(kwargs)))


if __name__ == "__main__":
    print("{} logs".format(count_items(nginx_coll)))
    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(
              method, count_items(nginx_coll, method=method)))
    print("{} status check".format(
          count_items(nginx_coll, method="GET", path="/status")))
