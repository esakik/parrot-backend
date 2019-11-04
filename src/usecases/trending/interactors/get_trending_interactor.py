import spotipy
from flask import current_app
from spotipy.oauth2 import SpotifyClientCredentials

from src.entities.trending import Trending
from src.exception.error import UnexpectedError
from src.usecases.trending.get_trending_usecase import GetTrendingUseCase
from src.usecases.trending.requests.get_trending_request import GetTrendingRequest
from src.usecases.trending.responses.get_trending_response import GetTrendingResponse


class GetTrendingInteractor(GetTrendingUseCase):
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
