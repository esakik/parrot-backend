import json

from flask import Blueprint, request

from src.adapters.gateways.library_gateway import LibraryGateway
from src.adapters.gateways.repositories.library_repository import LibraryRepository
from src.exception.error import ValidationError, UnexpectedError
from src.exception.handler import handle_validation_error, handle_success, handle_unexpected_error
from src.usecases.library.interactors.add_song_interactor import AddSongInteractor
from src.usecases.library.interactors.create_library_interactor import CreateLibraryInteractor
from src.usecases.library.interactors.get_library_interactor import GetLibraryInteractor
from src.usecases.library.requests.add_song_request import AddSongRequest
from src.usecases.library.requests.create_library_request import CreateLibraryRequest
from src.usecases.library.requests.get_library_request import GetLibraryRequest
from src.usecases.library.responses.add_song_response import AddSongResponse
from src.usecases.library.responses.create_library_response import CreateLibraryResponse
from src.usecases.library.responses.get_library_response import GetLibraryResponse

library = Blueprint("library", __name__, url_prefix="/library")


@library.route("/list", methods=["GET"])
def library_list():
    if request.method == "GET":
        user_id = request.args.get("user_id")

        try:
            gl_request = GetLibraryRequest(user_id)
        except ValidationError as e:
            return handle_validation_error(e)

        library_gateway: LibraryGateway = LibraryRepository()
        gl_interactor = GetLibraryInteractor(library_gateway)

        try:
            gl_response: GetLibraryResponse = gl_interactor.handle(gl_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(gl_response)


@library.route("/create", methods=["POST"])
def library_create():
    if request.method == "POST":
        data = json.loads(request.get_data())

        try:
            cl_request = CreateLibraryRequest(**data)
        except ValidationError as e:
            return handle_validation_error(e)

        library_gateway: LibraryGateway = LibraryRepository()
        cl_interactor = CreateLibraryInteractor(library_gateway)

        try:
            cl_response: CreateLibraryResponse = cl_interactor.handle(cl_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(cl_response)


@library.route("/add/song", methods=["POST"])
def library_add_song():
    if request.method == "POST":
        data = json.loads(request.get_data())

        try:
            as_request = AddSongRequest(**data)
        except ValidationError as e:
            return handle_validation_error(e)

        library_gateway: LibraryGateway = LibraryRepository()
        as_interactor = AddSongInteractor(library_gateway)

        try:
            as_response: AddSongResponse = as_interactor.handle(as_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(as_response)
