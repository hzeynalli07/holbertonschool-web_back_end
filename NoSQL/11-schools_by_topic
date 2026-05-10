#!/usr/bin/env python3
"""Find schools by topic."""


def schools_by_topic(mongo_collection, topic):
    """
    Return the list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object
        topic: topic searched

    Returns:
        List of schools with the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
