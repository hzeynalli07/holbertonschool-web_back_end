#!/usr/bin/env python3
"""
Log stats - provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """
    Displays stats about Nginx logs
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # 1. Ümumi log sayı
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Metodların statistikası
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        # Diqqət: Burada 4 boşluq (və ya \t) olmalıdır
        print(f"\tmethod {method}: {count}")

    # 3. Status check (GET metodu və /status yolu)
    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
