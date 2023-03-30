#!/usr/bin/env python3
"""Contains the function top_students
"""


def top_students(mongo_collection):
    """ returns all students sorted by average score
    """
    aggr_arr = [
        {
            "$project": {
                            "name": "$name",
                            "averageScore": {"$avg": "$topics.score"}
                        }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    docs = mongo_collection.aggregate(aggr_arr)
    return docs
