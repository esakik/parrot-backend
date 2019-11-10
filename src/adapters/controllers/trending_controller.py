from flask import Blueprint, request

from src.exception.error import ValidationError, UnexpectedError
from src.exception.handler import handle_validation_error, handle_unexpected_error, handle_success
from src.usecases.trending.get_trending_usecase import GetTrendingUseCase
from src.usecases.trending.interactors.get_trending_interactor import GetTrendingInteractor
from src.usecases.trending.requests.get_trending_request import GetTrendingRequest

trending = Blueprint("trending", __name__, url_prefix="/trending")


@trending.route("/list", methods=["GET"])
def trending_list():
    if request.method == "GET":
        limit = request.args.get("limit")
        offset = request.args.get("offset")

        try:
            get_trending_request = GetTrendingRequest(limit, offset)
        except ValidationError as e:
            return handle_validation_error(e)

        get_trending_usecase: GetTrendingUseCase = GetTrendingInteractor()

        try:
            get_trending_response = get_trending_usecase.handle(get_trending_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(get_trending_response)
