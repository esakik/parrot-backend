import spotipy
from flask import current_app
from spotipy.oauth2 import SpotifyClientCredentials

from src.entities.trending import Trending
from src.exception.errors import UnexpectedError
from src.request_objects.trending.get_trending_request import GetTrendingRequest
from src.response_objects.trending.get_trending_response import GetTrendingResponse
from src.use_cases.trending.get_trending_use_case import AbstractGetTrendingUseCase


class GetTrendingUseCase(AbstractGetTrendingUseCase):
    def __init__(self):
        client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(
            current_app.config["SPOTIFY_CLIENT_ID"], current_app.config["SPOTIFY_CLIENT_SECRET"]
        )

        self._spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def handle(self, request: GetTrendingRequest) -> GetTrendingResponse:
        results = self._spotify.new_releases(limit=request.limit, offset=request.offset)["albums"]["items"]

        if not results:
            raise UnexpectedError("Not found trending.")

        trending = [
            Trending(title=r["name"], external_url=r["artists"][0]["external_urls"]["spotify"]) for r in results
        ]

        return GetTrendingResponse(trending)
