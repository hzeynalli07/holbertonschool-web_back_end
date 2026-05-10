#!/usr/bin/env python3
"""
Log stats - new version with top 10 IPs
"""
from pymongo import MongoClient


def log_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Ümumi log sayı
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Metodların statistikası
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Status check sayı (method=GET və path=/status)
    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")

    # TOP 10 IP axtarışı (Aggregation Pipeline)
    print("IPs:")
    top_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": -1}},
        {"$limit": 10}
    ])

    for ip_data in top_ips:
        print(f"    {ip_data.get('_id')}: {ip_data.get('count')}")


if __name__ == "__main__":
    log_stats()
