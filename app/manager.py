import pandas as pd
from .fetcher import MongoFetcher
from .processor import Processor


class Manager:
    def __init__(self, fetcher: MongoFetcher, blacklist_path: str = "data/weapons.txt"):
        self.fetcher = fetcher
        self.blacklist_path = blacklist_path
        self._df: pd.DataFrame | None = None

    def _load_blacklist(self):
        try:
            with open(self.blacklist_path, "r", encoding="utf-8") as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            return []

    def run(self):
        data = self.fetcher.fetch_all()
        processor = Processor(data)
        blacklist = self._load_blacklist()
        self._df = processor.process(blacklist)
        return self._df

    def export_as_json(self):
        if self._df is None:
            self.run()
        return self._df.to_dict(orient="records")
