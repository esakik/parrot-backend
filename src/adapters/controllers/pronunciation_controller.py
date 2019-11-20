from flask import Blueprint, request

from src.adapters.controllers.handlers.handler import handle_success
from src.adapters.repositories.impl.bigquery_word_repository import BigQueryWordRepository
from src.request_objects.pronunciation.get_pronunciation_request import GetPronunciationRequest
from src.use_cases.pronunciation.impl.get_pronunciation_use_case import GetPronunciationUseCase

pronunciation = Blueprint("pronunciation", __name__, url_prefix="/pronunciation")


@pronunciation.route("/search", methods=["GET"])
def pronunciation_search():
    if request.method == "GET":
        words = request.args.get("words")

        req = GetPronunciationRequest(words)

        repo = BigQueryWordRepository()
        get_pronunciation = GetPronunciationUseCase(repo)

        res = get_pronunciation.handle(req)

        return handle_success(res)
