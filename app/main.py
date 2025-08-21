from fastapi import FastAPI
from .fetcher import MongoFetcher
from .manager import Manager

app = FastAPI(title="Hostile Tweets Processor", version="1.0.0")

_fetcher = MongoFetcher()
_manager = Manager(_fetcher)

@app.get("/get_data_processed")
def get_data_processed():
    return _manager.export_as_json()

@app.get("/health")
def health():
    return {"ok": True}
