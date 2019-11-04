from typing import List

from google.cloud import bigquery

from src.adapters.gateways.word_gateway import WordGateway
from src.entities.word import Word


class WordRepository(WordGateway):
    def __init__(self, dataset_id: str = "parrot", table_id: str = "words"):
        self._dataset_id = dataset_id
        self._table_id = table_id

        self._client = bigquery.Client()

    def find_by_names(self, names: List[str]) -> List[Word]:
        wanted_names = ", ".join([f"'{name}'" for name in names])
        query = (
            f"SELECT name, phonetic_symbol FROM `{self._dataset_id}.{self._table_id}` WHERE name in ({wanted_names})"
        )
        results = list(self._client.query(query, location="US"))

        return [Word(**r) for r in results]
