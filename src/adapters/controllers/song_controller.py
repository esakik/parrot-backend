from flask import Blueprint, request

from src.exception.error import ValidationError, UnexpectedError
from src.exception.handler import handle_validation_error, handle_unexpected_error, handle_success
from src.usecases.song.interactors.artist_search_interactor import ArtistSearchInteractor
from src.usecases.song.interactors.artist_title_search_interactor import ArtistTitleSearchInteractor
from src.usecases.song.interactors.title_search_interactor import TitleSearchInteractor
from src.usecases.song.requests.artist_search_request import ArtistSearchRequest
from src.usecases.song.requests.artist_title_search_request import ArtistTitleSearchRequest
from src.usecases.song.requests.title_search_request import TitleSearchRequest

song = Blueprint("song", __name__, url_prefix="/song")


@song.route("/artist-title/search", methods=["GET"])
def artist_title_search():
    if request.method == "GET":
        artist = request.args.get("artist")
        title = request.args.get("title")

        try:
            ats_request = ArtistTitleSearchRequest(artist, title)
        except ValidationError as e:
            return handle_validation_error(e)

        ats_interactor = ArtistTitleSearchInteractor()

        try:
            ats_response = ats_interactor.handle(ats_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(ats_response)


@song.route("/artist/search", methods=["GET"])
def artist_search():
    if request.method == "GET":
        artist = request.args.get("artist")

        try:
            as_request = ArtistSearchRequest(artist)
        except ValidationError as e:
            return handle_validation_error(e)

        as_interactor = ArtistSearchInteractor()

        try:
            as_response = as_interactor.handle(as_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(as_response)


@song.route("/title/search", methods=["GET"])
def title_search():
    if request.method == "GET":
        title = request.args.get("title")

        try:
            ts_request = TitleSearchRequest(title)
        except ValidationError as e:
            return handle_validation_error(e)

        ts_interactor = TitleSearchInteractor()

        try:
            ts_response = ts_interactor.handle(ts_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(ts_response)
