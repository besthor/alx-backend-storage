#!/usr/bin/env python3
""" Write a Python function that inserts a new document in a
    collection based on kwarg
"""


def insert_school(mongo_collection, **kwargs):
    """ mongo_collection will be the pymongo collection object
        Returns the new _id
    """
    document_id = mongo_collection.insert(kwargs)
    return document_id
