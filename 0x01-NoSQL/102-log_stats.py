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
    res = coll.find(kwargs)
    return len(list(res))


def top_10_ips(coll):
    """Return most visited ipsin log
    """
    aggr_arr = [
                {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}}, {"$limit": 10}
    ]
    res = coll.aggregate(aggr_arr)
    return res


def main():
    """Main function
    """
    ips = top_10_ips(nginx_coll)
    logs = count_items(nginx_coll)
    methods_count = [count_items(nginx_coll, method=mtd) for mtd in methods]
    status_count = count_items(nginx_coll, method="GET", path='/status')
    print("{} logs".format(count_items(nginx_coll)))
    print("Methods:")
    for i in range(len(methods)):
        print("\tmethod {}: {}".format(
              methods[i], methods_count[i]))
    print("{} status check".format(status_count))
    print("IPs:")
    for ip in ips:
        print('\t{}: {}'.format(ip.get('_id'), ip.get('count')))


if __name__ == "__main__":
    (main())
