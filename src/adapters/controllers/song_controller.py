from flask import Blueprint, request

from src.exception.error import ValidationError, UnexpectedError
from src.exception.handler import handle_validation_error, handle_unexpected_error, handle_success
from src.usecases.song.artist_search_usecase import ArtistSearchUseCase
from src.usecases.song.artist_title_search_usecase import ArtistTitleSearchUseCase
from src.usecases.song.interactors.artist_search_interactor import ArtistSearchInteractor
from src.usecases.song.interactors.artist_title_search_interactor import ArtistTitleSearchInteractor
from src.usecases.song.interactors.title_search_interactor import TitleSearchInteractor
from src.usecases.song.requests.artist_search_request import ArtistSearchRequest
from src.usecases.song.requests.artist_title_search_request import ArtistTitleSearchRequest
from src.usecases.song.requests.title_search_request import TitleSearchRequest
from src.usecases.song.title_search_usecase import TitleSearchUseCase

song = Blueprint("song", __name__, url_prefix="/song")


@song.route("/artist-title/search", methods=["GET"])
def artist_title_search():
    if request.method == "GET":
        artist = request.args.get("artist")
        title = request.args.get("title")

        try:
            artist_title_search_request = ArtistTitleSearchRequest(artist, title)
        except ValidationError as e:
            return handle_validation_error(e)

        artist_title_search_usecase: ArtistTitleSearchUseCase = ArtistTitleSearchInteractor()

        try:
            artist_title_search_response = artist_title_search_usecase.handle(artist_title_search_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(artist_title_search_response)


@song.route("/artist/search", methods=["GET"])
def artist_search():
    if request.method == "GET":
        artist = request.args.get("artist")

        try:
            artist_search_request = ArtistSearchRequest(artist)
        except ValidationError as e:
            return handle_validation_error(e)

        artist_search_usecase: ArtistSearchUseCase = ArtistSearchInteractor()

        try:
            artist_search_response = artist_search_usecase.handle(artist_search_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(artist_search_response)


@song.route("/title/search", methods=["GET"])
def title_search():
    if request.method == "GET":
        title = request.args.get("title")

        try:
            title_search_request = TitleSearchRequest(title)
        except ValidationError as e:
            return handle_validation_error(e)

        title_search_usecase: TitleSearchUseCase = TitleSearchInteractor()

        try:
            title_search_response = title_search_usecase.handle(title_search_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(title_search_response)
