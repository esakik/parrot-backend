from flask import Blueprint, request

from src.adapters.controllers.handlers.handler import handle_success
from src.request_objects.song.artist_search_request import ArtistSearchRequest
from src.request_objects.song.artist_title_search_request import ArtistTitleSearchRequest
from src.request_objects.song.title_search_request import TitleSearchRequest
from src.use_cases.song.impl.artist_search_use_case import ArtistSearchUseCase
from src.use_cases.song.impl.artist_title_search_use_case import ArtistTitleSearchUseCase
from src.use_cases.song.impl.title_search_use_case import TitleSearchUseCase

song = Blueprint("song", __name__, url_prefix="/song")


@song.route("/artist-title/search", methods=["GET"])
def artist_title_search():
    if request.method == "GET":
        artist = request.args.get("artist")
        title = request.args.get("title")

        req = ArtistTitleSearchRequest(artist, title)
        search_by_artist_and_title = ArtistTitleSearchUseCase()

        res = search_by_artist_and_title.handle(req)

        return handle_success(res)


@song.route("/artist/search", methods=["GET"])
def artist_search():
    if request.method == "GET":
        artist = request.args.get("artist")

        req = ArtistSearchRequest(artist)
        search_by_artist = ArtistSearchUseCase()

        res = search_by_artist.handle(req)

        return handle_success(res)


@song.route("/title/search", methods=["GET"])
def title_search():
    if request.method == "GET":
        title = request.args.get("title")

        req = TitleSearchRequest(title)
        search_by_title = TitleSearchUseCase()

        res = search_by_title.handle(req)

        return handle_success(res)
