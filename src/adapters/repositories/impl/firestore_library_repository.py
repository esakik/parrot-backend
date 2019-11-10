from firebase_admin import firestore

from src.adapters.repositories.library_repository import LibraryRepository
from src.entities.library import Library
from src.entities.song import Song


class FirestoreLibraryRepository(LibraryRepository):
    def __init__(self, table_name="libraries"):
        self._table_name = table_name
        self._db = firestore.client()

    def find_by_user_id(self, user_id: str) -> Library:
        doc_ref = self._db.collection(self._table_name).document(user_id)
        doc = doc_ref.get()

        songs = [Song(**song) for song in doc.to_dict()["songs"]]

        return Library(doc.id, songs)

    def insert(self, user_id: str) -> str:
        doc_ref = self._db.collection(self._table_name).document(user_id)
        doc_ref.set({"songs": []})

        return doc_ref.get().id

    def update(self, library: Library) -> str:
        doc_ref = self._db.collection(self._table_name).document(library.user_id)
        doc_ref.update({"songs": firestore.ArrayUnion([song.__dict__ for song in library.songs])})

        return doc_ref.get().id
