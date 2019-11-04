import spotipy
from flask import current_app
from spotipy.oauth2 import SpotifyClientCredentials

from src.entities.recommended import Recommended
from src.exception.error import UnexpectedError
from src.usecases.recommended.get_recommended_usecase import GetRecommendedUseCase
from src.usecases.recommended.requests.get_recommended_request import GetRecommendedRequest
from src.usecases.recommended.responses.get_recommended_response import GetRecommendedResponse


class GetRecommendedInteractor(GetRecommendedUseCase):
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
