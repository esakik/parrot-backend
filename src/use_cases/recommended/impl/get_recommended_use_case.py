import spotipy
from flask import current_app
from spotipy.oauth2 import SpotifyClientCredentials

from src.entities.recommended import Recommended
from src.exception.errors import UnexpectedError
from src.request_objects.recommended.get_recommended_request import GetRecommendedRequest
from src.response_objects.recommended.get_recommended_response import GetRecommendedResponse
from src.use_cases.recommended.get_recommended_use_case import AbstractGetRecommendedUseCase


class GetRecommendedUseCase(AbstractGetRecommendedUseCase):
    def __init__(self):
        client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(
            current_app.config["SPOTIFY_CLIENT_ID"], current_app.config["SPOTIFY_CLIENT_SECRET"]
        )

        self._spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def handle(self, request: GetRecommendedRequest) -> GetRecommendedResponse:
        results = self._spotify.new_releases(limit=request.limit, offset=request.offset)["albums"]["items"]

        if not results:
            raise UnexpectedError("Not found recommended.")

        recommended = [
            Recommended(
                artist=r["artists"][0]["name"],
                title=r["name"],
                jacket_image_url=r["images"][0]["url"],
                external_url=r["external_urls"]["spotify"],
            )
            for r in results
        ]

        return GetRecommendedResponse(recommended)
