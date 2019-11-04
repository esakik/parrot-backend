from flask import Blueprint, request

from src.exception.error import ValidationError, UnexpectedError
from src.exception.handler import handle_validation_error, handle_unexpected_error, handle_success
from src.usecases.trending.interactors.get_trending_interactor import GetTrendingInteractor
from src.usecases.trending.requests.get_trending_request import GetTrendingRequest

trending = Blueprint("trending", __name__, url_prefix="/trending")


@trending.route("/list", methods=["GET"])
def trending_list():
    if request.method == "GET":
        limit = request.args.get("limit")
        offset = request.args.get("offset")

        try:
            gt_request = GetTrendingRequest(limit, offset)
        except ValidationError as e:
            return handle_validation_error(e)

        gt_interactor = GetTrendingInteractor()

        try:
            gt_response = gt_interactor.handle(gt_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(gt_response)
