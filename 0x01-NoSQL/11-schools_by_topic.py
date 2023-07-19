#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [d for d in documents]
    return list_docs
