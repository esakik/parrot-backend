from flask import Blueprint, request

from src.adapters.gateways.repositories.word_repository import WordRepository
from src.adapters.gateways.word_gateway import WordGateway
from src.exception.error import ValidationError
from src.exception.handler import handle_validation_error, handle_success
from src.usecases.pronunciation.interactors.get_pronunciation_interactor import GetPronunciationInteractor
from src.usecases.pronunciation.requests.get_pronunciation_request import GetPronunciationRequest

pronunciation = Blueprint("pronunciation", __name__, url_prefix="/pronunciation")


@pronunciation.route("/search", methods=["GET"])
def pronunciation_search():
    if request.method == "GET":
        words = request.args.get("words")

        try:
            gp_request = GetPronunciationRequest(words)
        except ValidationError as e:
            return handle_validation_error(e)

        word_gateway: WordGateway = WordRepository()

        gp_interactor = GetPronunciationInteractor(word_gateway)

        gp_response = gp_interactor.handle(gp_request)

        return handle_success(gp_response)
