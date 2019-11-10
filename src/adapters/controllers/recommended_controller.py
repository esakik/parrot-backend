from flask import Blueprint, request

from src.exception.error import ValidationError, UnexpectedError
from src.exception.handler import handle_validation_error, handle_unexpected_error, handle_success
from src.usecases.recommended.get_recommended_usecase import GetRecommendedUseCase
from src.usecases.recommended.interactors.get_recommended_interactor import GetRecommendedInteractor
from src.usecases.recommended.requests.get_recommended_request import GetRecommendedRequest

recommended = Blueprint("recommended", __name__, url_prefix="/recommended")


@recommended.route("/list", methods=["GET"])
def recommended_list():
    if request.method == "GET":
        limit = request.args.get("limit")
        offset = request.args.get("offset")

        try:
            get_recommended_request = GetRecommendedRequest(limit, offset)
        except ValidationError as e:
            return handle_validation_error(e)

        get_recommended_usecase: GetRecommendedUseCase = GetRecommendedInteractor()

        try:
            get_recommended_response = get_recommended_usecase.handle(get_recommended_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(get_recommended_response)
