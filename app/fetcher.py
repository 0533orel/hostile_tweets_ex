import os
from pymongo import MongoClient
import pandas as pd


class MongoFetcher:
    def __init__(self, mongo_uri=None, db_name=None, collection_name=None):
        self.mongo_uri = mongo_uri or os.getenv("MONGO_URI")
        if not self.mongo_uri:
            raise ValueError("Incompatible MONGO_URI environment variable")

        self.db_name = db_name or os.getenv("MONGO_DB", "IranMalDB")
        self.collection_name = collection_name or os.getenv("MONGO_COLLECTION", "tweets")
        self.client = MongoClient(self.mongo_uri)
        self.collection = self.client[self.db_name][self.collection_name]

    def fetch_all(self):
        collection = self.collection.find({}, {"_id": 1, "Text": 1})
        rows = []
        for doc in collection:
            txt = doc.get("Text", "")
            if isinstance(txt, str) and txt.strip():
                rows.append({"id":str(doc.get("_id", "")), "original_text": txt})
        return pd.DataFrame(rows, columns=["id", "original_text"])