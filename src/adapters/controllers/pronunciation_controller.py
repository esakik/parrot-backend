from flask import Blueprint, request

from src.adapters.repositories.impl.bigquery_word_repository import BigQueryWordRepository
from src.adapters.repositories.word_repository import WordRepository
from src.exception.error import ValidationError
from src.exception.handler import handle_validation_error, handle_success
from src.usecases.pronunciation.get_pronunciation_usecase import GetPronunciationUseCase
from src.usecases.pronunciation.interactors.get_pronunciation_interactor import GetPronunciationInteractor
from src.usecases.pronunciation.requests.get_pronunciation_request import GetPronunciationRequest

pronunciation = Blueprint("pronunciation", __name__, url_prefix="/pronunciation")


@pronunciation.route("/search", methods=["GET"])
def pronunciation_search():
    if request.method == "GET":
        words = request.args.get("words")

        try:
            get_pronunciation_request = GetPronunciationRequest(words)
        except ValidationError as e:
            return handle_validation_error(e)

        word_repo: WordRepository = BigQueryWordRepository()

        get_pronunciation_usecase: GetPronunciationUseCase = GetPronunciationInteractor(word_repo)

        get_pronunciation_response = get_pronunciation_usecase.handle(get_pronunciation_request)

        return handle_success(get_pronunciation_response)
