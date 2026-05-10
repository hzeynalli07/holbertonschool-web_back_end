#!/usr/bin/env python3
"""
Top students - function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    pipeline = [
        {
            "$project": {
                "name": "$name",
                "topics": "$topics",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
