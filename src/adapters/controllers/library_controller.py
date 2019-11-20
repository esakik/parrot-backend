import json

from flask import Blueprint, request

from src.adapters.controllers.handlers.handler import handle_success
from src.adapters.repositories.impl.firestore_library_repository import FirestoreLibraryRepository
from src.request_objects.library.add_song_request import AddSongRequest
from src.request_objects.library.create_library_request import CreateLibraryRequest
from src.request_objects.library.get_library_request import GetLibraryRequest
from src.use_cases.library.impl.add_song_use_case import AddSongUseCase
from src.use_cases.library.impl.create_library_use_case import CreateLibraryUseCase
from src.use_cases.library.impl.get_library_use_case import GetLibraryUseCase

library = Blueprint("library", __name__, url_prefix="/library")


@library.route("/list", methods=["GET"])
def library_list():
    if request.method == "GET":
        user_id = request.args.get("user_id")

        req = GetLibraryRequest(user_id)

        repo = FirestoreLibraryRepository()
        get_library = GetLibraryUseCase(repo)

        res = get_library.handle(req)

        return handle_success(res)


@library.route("/create", methods=["POST"])
def library_create():
    if request.method == "POST":
        data = json.loads(request.get_data())

        req = CreateLibraryRequest(**data)

        repo = FirestoreLibraryRepository()
        create_library = CreateLibraryUseCase(repo)

        res = create_library.handle(req)

        return handle_success(res)


@library.route("/add/song", methods=["POST"])
def library_add_song():
    if request.method == "POST":
        data = json.loads(request.get_data())

        req = AddSongRequest(**data)

        repo = FirestoreLibraryRepository()
        add_song = AddSongUseCase(repo)

        res = add_song.handle(req)

        return handle_success(res)
