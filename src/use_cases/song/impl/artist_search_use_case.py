import lyricsgenius
from flask import current_app

from src.entities.song import Song
from src.exception.errors import UnexpectedError
from src.request_objects.song.artist_search_request import ArtistSearchRequest
from src.response_objects.song.artist_search_response import ArtistSearchResponse
from src.use_cases.song.artist_search_use_case import AbstractArtistSearchUseCase


class ArtistSearchUseCase(AbstractArtistSearchUseCase):
    def __init__(self):
        self._genius = lyricsgenius.Genius(current_app.config["GENIUS_TOKEN"])
        self._genius.verbose = False
        self._genius.remove_section_headers = True
        self._genius.skip_non_songs = False
        self._genius.excluded_terms = ["(Remix)", "(Live)"]

    def handle(self, request: ArtistSearchRequest) -> ArtistSearchResponse:
        artist = self._genius.search_artist(request.artist, max_songs=4, get_full_info=False)

        if not artist:
            raise UnexpectedError(f"Not found songs of {artist}.")

        songs = [
            Song(artist=song.artist, title=song.title, lyrics=song.lyrics, jacket_image_url=song.song_art_image_url)
            for song in artist.songs
        ]

        return ArtistSearchResponse(songs)
