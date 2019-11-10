import json

from flask import Blueprint, request

from src.adapters.repositories.impl.firestore_library_repository import FirestoreLibraryRepository
from src.adapters.repositories.library_repository import LibraryRepository
from src.exception.error import ValidationError, UnexpectedError
from src.exception.handler import handle_validation_error, handle_success, handle_unexpected_error
from src.usecases.library.add_song_usecase import AddSongUseCase
from src.usecases.library.create_library_usecase import CreateLibraryUseCase
from src.usecases.library.get_library_usecase import GetLibraryUseCase
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
            get_library_request = GetLibraryRequest(user_id)
        except ValidationError as e:
            return handle_validation_error(e)

        library_repo: LibraryRepository = FirestoreLibraryRepository()
        get_library_usecase: GetLibraryUseCase = GetLibraryInteractor(library_repo)

        try:
            get_library_response: GetLibraryResponse = get_library_usecase.handle(get_library_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(get_library_response)


@library.route("/create", methods=["POST"])
def library_create():
    if request.method == "POST":
        data = json.loads(request.get_data())

        try:
            create_library_request = CreateLibraryRequest(**data)
        except ValidationError as e:
            return handle_validation_error(e)

        library_repo: LibraryRepository = FirestoreLibraryRepository()
        create_library_usecase: CreateLibraryUseCase = CreateLibraryInteractor(library_repo)

        try:
            create_library_response: CreateLibraryResponse = create_library_usecase.handle(create_library_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(create_library_response)


@library.route("/add/song", methods=["POST"])
def library_add_song():
    if request.method == "POST":
        data = json.loads(request.get_data())

        try:
            add_song_request = AddSongRequest(**data)
        except ValidationError as e:
            return handle_validation_error(e)

        library_repo: LibraryRepository = FirestoreLibraryRepository()
        add_song_usecase: AddSongUseCase = AddSongInteractor(library_repo)

        try:
            add_song_response: AddSongResponse = add_song_usecase.handle(add_song_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(add_song_response)
