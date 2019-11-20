import lyricsgenius
from flask import current_app

from src.entities.song import Song
from src.exception.errors import UnexpectedError
from src.request_objects.song.artist_title_search_request import ArtistTitleSearchRequest
from src.response_objects.song.artist_title_search_response import ArtistTitleSearchResponse
from src.use_cases.song.artist_title_search_use_case import AbstractArtistTitleSearchUseCase


class ArtistTitleSearchUseCase(AbstractArtistTitleSearchUseCase):
    def __init__(self):
        self._genius = lyricsgenius.Genius(current_app.config["GENIUS_TOKEN"])
        self._genius.verbose = False
        self._genius.remove_section_headers = True
        self._genius.skip_non_songs = False
        self._genius.excluded_terms = ["(Remix)", "(Live)"]

    def handle(self, request: ArtistTitleSearchRequest) -> ArtistTitleSearchResponse:
        song = self._genius.search_song(request.title, request.artist)

        if not song:
            raise UnexpectedError(f"Not found {request.title} of {request.artist}.")

        songs = [
            Song(artist=song.artist, title=song.title, lyrics=song.lyrics, jacket_image_url=song.song_art_image_url)
        ]

        return ArtistTitleSearchResponse(songs)
